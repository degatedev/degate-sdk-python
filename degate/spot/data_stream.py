from degate.lib.utils import check_required_parameter


def newListenKey(self):
    return self.callDeGate("newListenKey")


def reNewListenKey(self, listenKey: str):
    check_required_parameter(listenKey, "listenKey")
    return self.callDeGate("reNewListenKey", {"listen_key": listenKey})


def deleteListenKey(self, listenKey: str):
    check_required_parameter(listenKey, "listenKey")
    return self.callDeGate("closeListenKey", {"listen_key": listenKey})