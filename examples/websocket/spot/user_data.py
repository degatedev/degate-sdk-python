#!/usr/bin/env python

import time
import logging
from degate.lib.utils import config_logging
from degate.spot import Spot as Client
from degate.websocket.spot.websocket_client import SpotWebsocketClient


config_logging(logging, logging.DEBUG)


def message_handler(message):
    if message is not None:
        print(message.decode("utf-8"))

AccountAddress = "0xba2b5feae299808b119fd410370d388b2fbf744b"
TradingKey = ""
AccountId = 2475

client = Client(AccountAddress, TradingKey, AccountId)

try:
    response = client.new_listen_key()
    print("Receive listen key : {}".format(response["listenKey"]))

    ws_client = SpotWebsocketClient()
    ws_client.start()
    ws_client.user_data(
        listen_key=response["listenKey"],
        id=87,
        callback=message_handler,
    )
    time.sleep(30000)
    logging.debug("closing ws connection")
    ws_client.stop()
except Exception as e:
    logging.error(e)
