from degate.websocket.websocket_client import DeGateWebsocketClient


class SpotWebsocketClient(DeGateWebsocketClient):
    def __init__(self, tokens=None, websocketBaseUrl=None):
        super().__init__(tokens, websocketBaseUrl)


    def subscribeTrade(self, symbol: str, id: int, callback, **kwargs):
        self.live_subscribe("trade", id, callback, symbol=symbol, **kwargs)


    def subscribeKline(self, symbol: str, id: int, interval: str, callback, **kwargs):
        self.live_subscribe("kline", id, callback, symbol=symbol, interval=interval)


    def subscribeTicker(self, id: int, callback, symbol=None, **kwargs):
        self.live_subscribe("ticker", id, callback, symbol=symbol, **kwargs)


    def subscribeBookTicker(self, id: int, callback, symbol=None, **kwargs):
        self.live_subscribe("bookTicker", id, callback, symbol=symbol, **kwargs)


    def subscribeDepth(self, symbol: str, id: int, level, speed, callback, **kwargs):
        self.live_subscribe("depth", id, callback, symbol=symbol, level=level, speed=speed, **kwargs)


    def subscribeDepthUpdate(self, symbol: str, id: int, speed, callback, **kwargs):
        self.live_subscribe("depthUpdate", id, callback, symbol=symbol, speed=speed, **kwargs)


    def subscribeUserData(self, listen_key: str, id: int, callback, **kwargs):
        self.live_subscribe("userData", id, callback,listen_key=listen_key, **kwargs)
