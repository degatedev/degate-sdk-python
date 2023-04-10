#!/usr/bin/env python

import logging
from degate.spot import Spot as Client
from degate.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

AccountAddress = "0xba2b5feae299808b119fd410370d388b2fbf744b"
AssetPrivateKey = ""
AccountId = 2475

try:
    ETH = {
        "id": 0,
        "symbol": "ETH",
    }
    client = Client(AccountAddress, AssetPrivateKey, AccountId, tokens=[ETH])
    logging.info(client.getBalance(asset="ETH"))
except Exception as e:
    logging.error(e)

try:
    client = Client(AccountAddress, AssetPrivateKey, AccountId)
    logging.info(client.getBalance())
except Exception as e:
    logging.error(e)
