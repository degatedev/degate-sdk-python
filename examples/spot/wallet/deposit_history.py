#!/usr/bin/env python

import logging
from degate.spot import Spot as Client
from degate.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

AccountAddress = "0x79e106A68DbA9B432718a65d0DD2798024104231"
AssetPrivateKey = ""
AccountId = 20

client = Client(AccountAddress,AssetPrivateKey,AccountId)

try:
    param = {"limit":10}
    logging.info(client.depositHistory(**param))
except Exception as e:
    logging.error(e)


