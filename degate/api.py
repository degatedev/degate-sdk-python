import json
import logging
from json import JSONDecodeError
from degate.error import ClientError, ServerError, DeGateError
import degate.lib.libgo as lib


class API(object):

    def __init__(
        self,
        accountAddress=None,
        assetPrivateKey=None,
        accountId=None,
        baseUrl=None,
        tokens=None,
        timeout=None,
        debug=False,
        show_header=False,
    ):
        self.accountAddress = accountAddress
        self.assetPrivateKey = assetPrivateKey
        self.accountId = accountId
        self.tokens = None
        self.timeout = timeout
        self.base_url = baseUrl
        if type(tokens) is list:
            self.tokens = tokens
        self.show_header = show_header

        config = {
            "BaseUrl": self.base_url,
            "AccountAddress": accountAddress,
            "AssetPrivateKey": assetPrivateKey,
            "AccountId": accountId,
            "Timeout": self.timeout,
            "Tokens": self.tokens,
            "Debug": debug,
            "ShowHeader":show_header,
        }
        self.AppConfig = json.dumps(config).encode("utf-8")
        self._logger = logging.getLogger(__name__)
        return

    def callDeGate(self, method, param=None):
        if param is None:
            param = ""
        else:
            param = json.dumps(param).encode("utf-8")
        response = lib.libgo.send_request(self.AppConfig, method.encode("utf-8"), param)
        if response is not None:
            response = response.decode("utf-8")
            self.handleException(response)
            response = json.loads(response)
            data = response.get("data", None)
            result = {}
            if self.show_header:
                result["header"] = response.get("header",None)
            if len(result) != 0:
                result["data"] = data
                return result
            return data

    def handleException(self, response_text):
        try:
            response = json.loads(response_text)
        except JSONDecodeError:
            raise DeGateError(response_text)
        status_code = response["http_status_code"]
        if status_code < 400:
            if response['code'] != 0:
                raise ServerError(status_code, "code:{} message:{}".format(response["code"], response["message"]))
            return
        if 400 <= status_code < 500:
            if not response["http_body_text"]:
                raise ClientError(status_code, response["code"], response["message"], None)
            else:
                raise ClientError(status_code, None, response["http_body_text"], None)
        if not response["http_body_text"]:
            raise ServerError(status_code, "code:{} message:{}".format(response["code"], response["message"]))
        else:
            raise ServerError(status_code, response["http_body_text"])

