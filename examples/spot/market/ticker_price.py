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
USDT = {
    "id": 9,
    "symbol": "USDT",
}

spot_client = Client(tokens=[ETH,USDC,USDT])

try:
    logging.info(spot_client.tickerPrice("ETHUSDC,ETHUSDT"))
except Exception as e:
    logging.error(e)

