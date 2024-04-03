import pytest
import os, json
import logging

class ColorFormatter(logging.Formatter):
  GREEN = '\033[92m'
#   LIGHT_RED = '\033[91m'
#   YELLOW = '\033[93m'
  RESET = '\033[0m'

  FORMATS = {
    # logging.DEBUG: GREEN + '%(message)s' + RESET,
    logging.INFO: GREEN + '%(message)s' + RESET,
    # logging.WARNING: GREEN + '%(message)s' + RESET,
    # logging.ERROR: GREEN + '%(message)s' + RESET,
    # logging.CRITICAL: GREEN + '%(message)s' + RESET
  }

@pytest.fixture(scope='session', autouse=True)
def setup_logging():
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(ColorFormatter())
    root_logger.addHandler(console_handler)
