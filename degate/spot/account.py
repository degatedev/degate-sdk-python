from degate.lib.utils import check_required_parameter
from degate.lib.utils import check_required_parameters

def new_order(self, symbol: str, side: str, type: str, **kwargs):
    check_required_parameters([[symbol, "symbol"], [side, "side"], [type, "type"]])
    params = {"symbol": symbol, "side": side, "type": type, "source": "pythonSdk", **kwargs}
    return self.callDeGate("newOrder", params)

def cancel_order(self, orderId: str, **kwargs):
    check_required_parameter(orderId, "orderId")
    payload = {"orderId": orderId, **kwargs}
    return self.callDeGate("cancelOrder", payload)

def cancel_order_on_chain(self,orderId: str, **kwargs):
    check_required_parameter(orderId, "orderId")
    payload = {"orderId": orderId, **kwargs}
    return self.callDeGate("cancelOrderOnChain",payload)

def cancel_open_orders(self,includeGrid:bool = False,**kwargs):
    payload = {"includeGrid": includeGrid, **kwargs}
    return self.callDeGate("cancelOpenOrders",payload)

def get_order(self, orderId=None, **kwargs):
    check_required_parameter(orderId, "orderId")
    payload = {"orderId": orderId, **kwargs}
    return self.callDeGate("order", payload)

def get_open_orders(self, symbol=None, **kwargs):
    payload = {"symbol": symbol, **kwargs}
    return self.callDeGate("openOrders", payload)

def get_history_orders(self, symbol: str, **kwargs):
    check_required_parameter(symbol, "symbol")
    payload = {"symbol": symbol, **kwargs}
    return self.callDeGate("historyOrders", payload)

def account(self):
    return self.callDeGate("account")

def my_trades(self, symbol: str, **kwargs):
    check_required_parameter(symbol, "symbol")
    payload = {"symbol": symbol, **kwargs}
    return self.callDeGate("myTrades", payload)
