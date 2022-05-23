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
my_client.trade(
    symbol="ETHUSDC",
    interval="1m",
    id=1,
    callback=message_handler,
)

time.sleep(30000)
logging.debug("closing ws connection")
my_client.stop()
