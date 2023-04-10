#!/usr/bin/env python

import logging
from degate.spot import Spot as Client
from degate.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

AccountAddress = "0xba2b5feae299808b119fd410370d388b2fbf744b"
AssetPrivateKey = ""
AccountId = 7
ETH = {
    "id": 0,
    "symbol": "ETH",
}
USDC = {
    "id": 2,
    "symbol": "USDC",
}

client = Client(AccountAddress, AssetPrivateKey, AccountId,tokens=[ETH,USDC])

try:
    response = client.getHistoryOrders("ETHUSDC",limit=3,orderId="585379933730473514117684527105")
    logging.info(response)
except Exception as e:
    logging.error(e)

