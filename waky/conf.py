import logging
import os
from pathlib import Path

import yaml
from waky.logging_config import configure_logging

DEFAULT_CONF_PATH = Path.home() / ".config" / "waky" / "waky.yml"
DEFAULT_CONF = {"devices": {"127.0.0.1": "", "nlandier-desktop": "", "nlandier-desktop": "", "rpi01": "", "rpi02": ""}}

configure_logging()
logger = logging.getLogger(__name__)


class Config:
    def __init__(self):
        try:
            with open(DEFAULT_CONF_PATH, "r") as file:
                logger.debug(f"Configuration file found: {DEFAULT_CONF_PATH}")
                conf = yaml.full_load(file)
                logger.debug(f"Configuration file: {conf}")
        except FileNotFoundError:
            logger.debug("configuration file not found")
            try:
                os.mkdir(os.path.dirname(DEFAULT_CONF_PATH))
            except FileExistsError:
                logger.debug("Configuration folder already exists")
            with open(DEFAULT_CONF_PATH, "w") as file:
                logger.debug("configuration file created with default values")
                conf = DEFAULT_CONF
                yaml.dump(DEFAULT_CONF, file)
        self.devices = conf["devices"]

    def __repr__(self):
        return str(vars(self))


if __name__ == "__main__":
    config = Config()
    logging.info(config)
