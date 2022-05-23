from degate.websocket.websocket_client import DeGateWebsocketClient


class SpotWebsocketClient(DeGateWebsocketClient):
    def __init__(self, tokens=None, stream_url=None):
        super().__init__(tokens, stream_url)


    def trade(self, symbol: str, id: int, callback, **kwargs):
        self.live_subscribe("trade", id, callback, symbol=symbol, **kwargs)


    def kline(self, symbol: str, id: int, interval: str, callback, **kwargs):
        self.live_subscribe("kline", id, callback, symbol=symbol, interval=interval)


    def ticker(self, id: int, callback, symbol=None, **kwargs):
        self.live_subscribe("ticker", id, callback, symbol=symbol, **kwargs)


    def book_ticker(self, id: int, callback, symbol=None, **kwargs):
        self.live_subscribe("bookTicker", id, callback, symbol=symbol, **kwargs)


    def partial_book_depth(self, symbol: str, id: int, level, speed, callback, **kwargs):
        self.live_subscribe("depth", id, callback, symbol=symbol, level=level, speed=speed, **kwargs)


    def diff_book_depth(self, symbol: str, id: int, speed, callback, **kwargs):
        self.live_subscribe("depthUpdate", id, callback, symbol=symbol, speed=speed, **kwargs)


    def user_data(self, listen_key: str, id: int, callback, **kwargs):
        self.live_subscribe("userData", id, callback,listen_key=listen_key, **kwargs)
