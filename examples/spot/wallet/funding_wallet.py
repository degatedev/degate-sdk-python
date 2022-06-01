#!/usr/bin/env python

import logging
from degate.spot import Spot as Client
from degate.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

AccountAddress = "0xba2b5feae299808b119fd410370d388b2fbf744b"
AppPrivateKey = "2632894725898118267240653043394494434953414364053947631502368954038496915496"
AccountId = 2475

try:
    ETH = {
        "id": 0,
        "symbol": "ETH",
    }
    client = Client(AccountAddress, AppPrivateKey, AccountId, tokens=[ETH])
    logging.info(client.funding_wallet(asset="ETH"))
except Exception as e:
    logging.error(e)

try:
    client = Client(AccountAddress, AppPrivateKey, AccountId)
    logging.info(client.funding_wallet())
except Exception as e:
    logging.error(e)
