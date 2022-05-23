#!/usr/bin/env python

import logging
from degate.spot import Spot as Client
from degate.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

ETH = {
    "id": 0,
    "symbol": "ETH",
}
USDC = {
    "id": 8,
    "symbol": "USDC",
}

client = Client(tokens=[ETH,USDC])

try:
    logging.info(client.klines("ETHUSDC", "1m", limit=10))
    logging.info(client.klines("ETHUSDC", "1h", limit=10))
except Exception as e:
    logging.error(e)

