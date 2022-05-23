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

spot_client = Client(tokens=[ETH,USDC])

try:
    logging.info(spot_client.ticker_price("ETHUSDC"))
except Exception as e:
    logging.error(e)

