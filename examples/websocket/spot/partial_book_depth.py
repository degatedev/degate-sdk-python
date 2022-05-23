#!/usr/bin/env python

import time
import logging
from degate.lib.utils import config_logging
from degate.websocket.spot.websocket_client import SpotWebsocketClient as Client

config_logging(logging, logging.DEBUG)

ETH = {
    "id": 0,
    "symbol": "ETH",
}
USDC = {
    "id": 8,
    "symbol": "USDC",
}

def message_handler(message):
    if message is not None:
        print(message.decode("utf-8"))

my_client = Client(tokens=[ETH,USDC])
my_client.start()
my_client.partial_book_depth(
    symbol="ETHUSDC",
    level=5,
    speed=100,
    id=39,
    callback=message_handler,
)

# time.sleep(2)
#
# my_client.partial_book_depth(
#     symbol="btcusdt",
#     level=10,
#     speed=100,
#     id=2,
#     callback=message_handler,
# )

time.sleep(3)
logging.debug("closing ws connection")
my_client.stop()
logging.debug("finish")
