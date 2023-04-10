from degate.api import API


class Spot(API):
    def __init__(self, accountAddress=None, assetPrivateKey=None, accountId=None, **kwargs):
        super().__init__(accountAddress, assetPrivateKey, accountId, **kwargs)

    # MARKETS
    from degate.spot.market import ping
    from degate.spot.market import time
    from degate.spot.market import exchangeInfo
    from degate.spot.market import tokenList
    from degate.spot.market import depth
    from degate.spot.market import trades
    from degate.spot.market import tradesHistory
    from degate.spot.market import klines
    from degate.spot.market import ticker24
    from degate.spot.market import tickerPrice
    from degate.spot.market import bookTicker

    # ACCOUNT
    from degate.spot.account import newOrder
    from degate.spot.account import cancelOrder
    from degate.spot.account import cancelOrderOnChain
    from degate.spot.account import cancelOpenOrders
    from degate.spot.account import getOrder
    from degate.spot.account import getOpenOrders
    from degate.spot.account import getHistoryOrders
    from degate.spot.account import account
    from degate.spot.account import myTrades

    # STREAMS
    from degate.spot.data_stream import newListenKey
    from degate.spot.data_stream import reNewListenKey
    from degate.spot.data_stream import deleteListenKey

    # WALLET
    from degate.spot.wallet import withdraw
    from degate.spot.wallet import depositHistory
    from degate.spot.wallet import withdrawHistory
    from degate.spot.wallet import transfer
    from degate.spot.wallet import transferHistory
    from degate.spot.wallet import trade_fee
    from degate.spot.wallet import gasFee
    from degate.spot.wallet import getBalance
