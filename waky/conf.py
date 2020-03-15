import logging
import os
from pathlib import Path

import yaml
from waky.logging_config import configure_logging

DEFAULT_CONF_PATH = Path.home() / ".config" / "waky" / "waky.yml"
DEFAULT_CONF = {
    "debug": True,
    "devices": {"127.0.0.1": "", "nlandier-desktop": "", "nlandier-desktop": "", "rpi01": "", "rpi02": ""},
    "listen": "0.0.0.0",
    "port": 8888,
}

configure_logging()
logger = logging.getLogger(__name__)


class Config:
    def __init__(self):
        try:
            with open(DEFAULT_CONF_PATH, "r") as file:
                logger.debug(f"Configuration file found: {DEFAULT_CONF_PATH}")
                self.conf = yaml.full_load(file)
                logger.debug(f"Configuration file: {self.conf}")
        except FileNotFoundError:
            logger.debug("configuration file not found")
            try:
                os.mkdir(os.path.dirname(DEFAULT_CONF_PATH))
            except FileExistsError:
                logger.debug("Configuration folder already exists")
            with open(DEFAULT_CONF_PATH, "w") as file:
                logger.debug("configuration file created with default values")
                self.conf = DEFAULT_CONF
                yaml.dump(DEFAULT_CONF, file)

    def __getattr__(self, name):
        return self.conf[name]

    def __repr__(self):
        return str(vars(self))


if __name__ == "__main__":
    config = Config()
    logging.info(config)
