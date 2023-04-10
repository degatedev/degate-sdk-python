from degate.lib.utils import check_required_parameters


def withdraw(self, coin: str, amount: float, address: str, privateKey: str, fee="", **kwargs):
    check_required_parameters(
        [[coin, "coin"], [amount, "amount"], [address, "address"], [privateKey, "privateKey"]]
    )
    payload = {"coin": coin, "amount": amount, "address": address, "privateKey": privateKey, "fee": fee, **kwargs}
    return self.callDeGate("withdraw", payload)


def transfer(self, asset: str, amount: float, address: str, privateKey: str, fee="", **kwargs):
    check_required_parameters(
        [[asset, "asset"], [amount, "amount"], [address, "address"], [privateKey, "privateKey"]]
    )
    payload = {"asset": asset, "amount": amount, "address": address, "privateKey":privateKey, "fee": fee, **kwargs}
    return self.callDeGate("transfer", payload)


def depositHistory(self, **kwargs):
    return self.callDeGate("deposits", kwargs)


def withdrawHistory(self, **kwargs):
    return self.callDeGate("withdraws", kwargs)


def transferHistory(self, **kwargs):
    return self.callDeGate("transfers", kwargs)


def trade_fee(self, symbol: str, **kwargs):
    payload = {"symbol": symbol, **kwargs}
    return self.callDeGate("tradeFee", payload)

def gasFee(self, **kwargs):
    return self.callDeGate("gasFee", kwargs)


def getBalance(self,asset=None, **kwargs):
    payload = {"asset": asset, **kwargs}
    return self.callDeGate("balance",payload)
