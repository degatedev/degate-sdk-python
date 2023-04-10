#!/usr/bin/env python

import logging
from degate.spot import Spot as Client
from degate.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

AccountAddress = "0xba2b5feae299808b119fd410370d388b2fbf744b"
AssetPrivateKey = ""
AccountId = 2475
ETH = {
    "id": 0,
    "symbol": "ETH",
}

client = Client(AccountAddress, AssetPrivateKey, AccountId, tokens=[ETH])

try:
    response = client.transfer(asset="ETH", amount=0.0001, address="0x5ddc2c634954e7e1133aeff98e6c7e7b034e00d4", privateKey="")
    logging.info(response)
except Exception as e:
    logging.error(e)

