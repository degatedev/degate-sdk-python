from twisted.internet import reactor

from degate.websocket.degate_socket_manager import DeGateSocketManager


class DeGateWebsocketClient(DeGateSocketManager):
    def __init__(self, tokens, websocketBaseUrl):
        super().__init__(tokens, websocketBaseUrl)

    def stop(self):
        try:
            self.close()
        finally:
            reactor.stop()


    def _single_stream(self, stream):
        if isinstance(stream, str):
            return True
        elif isinstance(stream, list):
            return False
        else:
            raise ValueError("Invalid stream name, expect string or array")


    def live_subscribe(self, stream, id, callback, **kwargs):
        data = {"id": id, **kwargs}
        return self._start_socket(stream, data, callback)


    def instant_subscribe(self, stream, callback, **kwargs):
        data = {"stream": stream, **kwargs}
        return self._start_socket("combined", data, callback)