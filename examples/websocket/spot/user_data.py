#!/usr/bin/env python

import time
import logging
from degate.lib.utils import config_logging
from degate.spot import Spot as Client
from degate.websocket.spot.websocket_client import SpotWebsocketClient as WsClient


config_logging(logging, logging.DEBUG)


def message_handler(message):
    if message is not None:
        print(message.decode("utf-8"))

AccountAddress = "0xba2b5feae299808b119fd410370d388b2fbf744b"
AssetPrivateKey = ""
AccountId = 7

client = Client(AccountAddress, AssetPrivateKey, AccountId)

try:
    response = client.newListenKey()
    print("Receive listen key : {}".format(response["listenKey"]))

    wsClient = WsClient()
    wsClient.start()
    wsClient.subscribeUserData(
        listen_key=response["listenKey"],
        id=87,
        callback=message_handler,
    )
    time.sleep(30000)
    logging.debug("closing ws connection")
    wsClient.stop()
except Exception as e:
    logging.error(e)
