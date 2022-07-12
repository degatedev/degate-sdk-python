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
    response = client.close_listen_key(
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2NvdW50X2lkIjoyNDc1LCJleHAiOjEwODc2MjYzMzYzLCJvcmlnX2F0IjoxNjUyODkxMzI2LCJzb3VyY2VfaXAiOiIxNS4xNjQuMjI3LjIyMCJ9.XgsjcCO1liZS_Sqic5ll4H4ZQ6Y6GyUbn1YN02TAoqE")
    logging.info(response)
except Exception as e:
    logging.error(e)

