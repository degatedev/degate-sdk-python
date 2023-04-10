import json
import logging
import threading
from json import JSONDecodeError
from twisted.internet import reactor
from twisted.internet.error import ReactorAlreadyRunning

import degate.lib.libgo as lib
from degate.error import DeGateError

class DeGateSocketManager(threading.Thread):
    def __init__(self, tokens, websocketBaseUrl):
        threading.Thread.__init__(self)

        self.factories = {}
        self._connected_event = threading.Event()
        self.tokens = tokens
        self.websocketBaseUrl = websocketBaseUrl
        self._conns = {}
        self._connAgents = []
        self._user_callback = None
        self._logger = logging.getLogger(__name__)
        self.callbacks = []
        config = {
            "WebsocketBaseUrl": self.websocketBaseUrl,
            "Tokens": self.tokens,
            "Debug": False,
        }
        self.AppConfig = json.dumps(config).encode("utf-8")


    def _start_socket(self, stream, payload, callback, is_combined=False, is_live=True):
        self._call_degate(stream, payload, callback)


    def stop_socket(self, conn_key):
        if conn_key not in self._connAgents:
            return
        self._call_degate("stop", {"client": conn_key}, None)

    def run(self):
        try:
            reactor.run(installSignalHandlers=False)
        except ReactorAlreadyRunning:
            # Ignore error about reactor already running
            pass

    def close(self):
        for key in self._connAgents:
            self.stop_socket(key)
        self._connAgents = []
        self.callbacks = []

    def _call_degate(self, method, param, callback):
        if param is None:
            param = ""
        else:
            param = json.dumps(param).encode("utf-8")
        cb = None
        if callback is not None:
            cb = lib.CGOFunc(callback)
            self.callbacks.append(cb)
        response = lib.libgo.send_subscribe(self.AppConfig, method.encode("utf-8"), param, cb)
        if response is not None:
            response = response.decode("utf-8")
            try:
                response = json.loads(response)
                self._connAgents.append(response["client"])
            except JSONDecodeError:
                raise DeGateError(response)

