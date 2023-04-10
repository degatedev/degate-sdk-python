from degate.lib.utils import check_required_parameter
from degate.lib.utils import check_required_parameters


def ping(self):
    return self.callDeGate("ping")


def time(self):
    return self.callDeGate("time")


def exchangeInfo(self):
    return self.callDeGate("exchangeInfo")


def tokenList(self, symbols: str, **kwargs):
    check_required_parameter(symbols, "symbols")
    params = {"symbols": symbols, **kwargs}
    return self.callDeGate("tokens", params)


def depth(self, symbol: str, **kwargs):
    check_required_parameter(symbol, "symbol")
    params = {"symbol": symbol, **kwargs}
    return self.callDeGate("depth", params)


def trades(self, symbol: str, **kwargs):
    check_required_parameter(symbol, "symbol")
    params = {"symbol": symbol, **kwargs}
    return self.callDeGate("lastedTrades", params)


def tradesHistory(self, symbol: str, **kwargs):
    check_required_parameter(symbol, "symbol")
    params = {"symbol": symbol, **kwargs}
    return self.callDeGate("historyTrades", params)


def klines(self, symbol: str, interval: str, **kwargs):
    check_required_parameters([[symbol, "symbol"], [interval, "interval"]])
    params = {"symbol": symbol, "interval": interval, **kwargs}
    return self.callDeGate("klines", params)


def ticker24(self, symbol: str):
    check_required_parameter(symbol, "symbol")
    params = {
        "symbol": symbol,
    }
    return self.callDeGate("ticker", params)


def tickerPrice(self, symbol: str):
    check_required_parameter(symbol, "symbol")
    params = {
        "symbol": symbol,
    }
    return self.callDeGate("tickerPrice", params)


def bookTicker(self, symbol: str):
    check_required_parameter(symbol, "symbol")
    params = {
        "symbol": symbol
    }
    return self.callDeGate("bookTicker", params)
