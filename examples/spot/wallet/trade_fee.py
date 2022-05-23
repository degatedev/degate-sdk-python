#!/usr/bin/env python

import logging
from degate.spot import Spot as Client
from degate.lib.utils import config_logging

config_logging(logging, logging.DEBUG)
ETH = {
    "id": 0,
    "symbol": "ETH",
}
client = Client(tokens=[ETH])

try:
    logging.info(client.trade_fee("ETH"))
except Exception as e:
    logging.error(e)


