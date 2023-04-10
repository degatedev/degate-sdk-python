from degate.lib.utils import check_required_parameter
from degate.lib.utils import check_required_parameters

def newOrder(self, symbol: str, side: str, type: str, **kwargs):
    check_required_parameters([[symbol, "symbol"], [side, "side"], [type, "type"]])
    params = {"symbol": symbol, "side": side, "type": type, "source": "pythonSdk", **kwargs}
    return self.callDeGate("newOrder", params)

def cancelOrder(self, orderId = None, origClientOrderId=None):
    payload = {"orderId": orderId, "origClientOrderId":origClientOrderId}
    return self.callDeGate("cancelOrder", payload)

def cancelOrderOnChain(self, orderId=None, origClientOrderId=None):
    payload = {"orderId": orderId, "origClientOrderId":origClientOrderId}
    return self.callDeGate("cancelOrderOnChain",payload)

def cancelOpenOrders(self,includeGrid:bool = False,**kwargs):
    payload = {"includeGrid": includeGrid, **kwargs}
    return self.callDeGate("cancelOpenOrders",payload)

def getOrder(self, orderId=None,origClientOrderId=None):
    payload = {"orderId": orderId,"origClientOrderId": origClientOrderId}
    return self.callDeGate("order", payload)

def getOpenOrders(self, symbol=None, **kwargs):
    payload = {"symbol": symbol, **kwargs}
    return self.callDeGate("openOrders", payload)

def getHistoryOrders(self, symbol: str, **kwargs):
    check_required_parameter(symbol, "symbol")
    payload = {"symbol": symbol, **kwargs}
    return self.callDeGate("historyOrders", payload)

def account(self):
    return self.callDeGate("account")

def myTrades(self, symbol: str, **kwargs):
    check_required_parameter(symbol, "symbol")
    payload = {"symbol": symbol, **kwargs}
    return self.callDeGate("myTrades", payload)
