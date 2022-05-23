#!/usr/bin/env python

import logging
from degate.spot import Spot as Client
from degate.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

AccountAddress = "0xba2b5feae299808b119fd410370d388b2fbf744b"
AppPrivateKey = ""
AccountId = 2475

client = Client(AccountAddress, AppPrivateKey, AccountId)

try:
    response = client.cancel_open_orders()
    logging.info(response)
except Exception as e:
    logging.error(e)