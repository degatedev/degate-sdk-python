#!/usr/bin/env python

import logging
from degate.spot import Spot as Client
from degate.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

AccountAddress = "0xba2b5feae299808b119fd410370d388b2fbf744b"
TradingKey = ""
AccountId = 2475
ETH = {
    "id": 0,
    "symbol": "ETH",
}
USDC = {
    "id": 8,
    "symbol": "USDC",
}

client = Client(AccountAddress, TradingKey, AccountId,tokens=[ETH,USDC])

try:
    response = client.get_open_orders("ETHUSDC")
    logging.info(response)
except Exception as e:
    logging.error(e)

