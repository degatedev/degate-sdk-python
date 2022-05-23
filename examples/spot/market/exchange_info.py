import logging
from degate.spot import Spot as Client
from degate.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

client = Client()

try:
    logging.info(client.exchange_info())
except Exception as e:
    logging.error(e)

