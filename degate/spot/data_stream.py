from degate.lib.utils import check_required_parameter


def new_listen_key(self):
    return self.callDeGate("newListenKey")


def renew_listen_key(self, listenKey: str):
    check_required_parameter(listenKey, "listenKey")
    return self.callDeGate("reNewListenKey", {"listen_key": listenKey})


def close_listen_key(self, listenKey: str):
    check_required_parameter(listenKey, "listenKey")
    return self.callDeGate("closeListenKey", {"listen_key": listenKey})