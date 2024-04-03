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

  def format(self, record):
    log_fmt = self.FORMATS.get(record.levelno)
    formatter = logging.Formatter(log_fmt)
    return formatter.format(record)

@pytest.fixture(scope='session', autouse=True)
def setup_logging():
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(ColorFormatter())
    root_logger.addHandler(console_handler)

# number_of_scenarios = []

# @pytest.hookimpl
# def pytest_bdd_before_scenario(scenario):
#     number_of_scenarios.append(scenario.name)
#     logging.info(f"[Scenario Name]: {scenario.name}")

# @pytest.hookimpl
# def pytest_bdd_after_scenario(scenario):
#     logging.info(f"[Executed Scenarios]: {scenario.name}")

# @pytest.hookimpl
# def pytest_bdd_before_step(step):
#     logging.info(f"[Step Name]: {step.name}")