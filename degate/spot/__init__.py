from degate.api import API


class Spot(API):
    def __init__(self, accountAddress=None, tradingKey=None, accountId=None, **kwargs):
        super().__init__(accountAddress, tradingKey, accountId, **kwargs)

    # MARKETS
    from degate.spot.market import ping
    from degate.spot.market import time
    from degate.spot.market import exchange_info
    from degate.spot.market import get_tokens
    from degate.spot.market import depth
    from degate.spot.market import trades
    from degate.spot.market import historical_trades
    from degate.spot.market import klines
    from degate.spot.market import ticker_24hr
    from degate.spot.market import ticker_price
    from degate.spot.market import book_ticker

    # ACCOUNT
    from degate.spot.account import new_order
    from degate.spot.account import cancel_order
    from degate.spot.account import cancel_order_on_chain
    from degate.spot.account import cancel_open_orders
    from degate.spot.account import get_order
    from degate.spot.account import get_open_orders
    from degate.spot.account import get_history_orders
    from degate.spot.account import account
    from degate.spot.account import my_trades

    # STREAMS
    from degate.spot.data_stream import new_listen_key
    from degate.spot.data_stream import renew_listen_key
    from degate.spot.data_stream import close_listen_key

    # WALLET
    from degate.spot.wallet import withdraw
    from degate.spot.wallet import deposit_history
    from degate.spot.wallet import withdraw_history
    from degate.spot.wallet import transfer
    from degate.spot.wallet import transfer_history
    from degate.spot.wallet import trade_fee
    from degate.spot.wallet import gas_fee
    from degate.spot.wallet import funding_wallet
