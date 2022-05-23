from degate.lib.utils import check_required_parameter
from degate.lib.utils import check_required_parameters


def ping(self):
    return self.callDeGate("ping")


def time(self):
    return self.callDeGate("time")


def exchange_info(self):
    return self.callDeGate("exchangeInfo")


def get_tokens(self, symbols: str, **kwargs):
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


def historical_trades(self, symbol: str, **kwargs):
    check_required_parameter(symbol, "symbol")
    params = {"symbol": symbol, **kwargs}
    return self.callDeGate("historyTrades", params)


def klines(self, symbol: str, interval: str, **kwargs):
    check_required_parameters([[symbol, "symbol"], [interval, "interval"]])
    params = {"symbol": symbol, "interval": interval, **kwargs}
    return self.callDeGate("klines", params)


def ticker_24hr(self, symbol: str):
    check_required_parameter(symbol, "symbol")
    params = {
        "symbol": symbol,
    }
    return self.callDeGate("ticker", params)


def ticker_price(self, symbol: str):
    check_required_parameter(symbol, "symbol")
    params = {
        "symbol": symbol,
    }
    return self.callDeGate("tickerPrice", params)


def book_ticker(self, symbol: str):
    check_required_parameter(symbol, "symbol")
    params = {
        "symbol": symbol
    }
    return self.callDeGate("bookTicker", params)
