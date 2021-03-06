#!/usr/bin/env python

import logging
from degate.spot import Spot as Client
from degate.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

AccountAddress = "0xba2b5feae299808b119fd410370d388b2fbf744b"
TradingKey = ""
AccountId = 2475

client = Client(AccountAddress, TradingKey, AccountId)

try:
    response = client.get_order(orderId="196120192698583504448505788760278")
    logging.info(response)
except Exception as e:
    logging.error(e)

