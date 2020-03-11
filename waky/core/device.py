import logging
import socket
from datetime import datetime
from threading import RLock, Thread

import humanize
from getmac import get_mac_address
from ping3 import ping

logger = logging.getLogger(__name__)


class Device:
    def __init__(self, hostname):
        self.hostname = hostname
        self.ip = None
        self.mac = None
        self.last_ping_ms = None
        self.last_check = None
        self.refresh()

    def refresh(self):
        def refresh_thread_function():
            try:
                self.ip = socket.gethostbyname(self.hostname)
                self.mac = get_mac_address(hostname=self.hostname)
                self.last_ping_ms = ping(self.hostname, unit="ms", timeout=5)
            except socket.gaierror:
                logger.debug(f"Unknown host")
            finally:
                self.last_check = datetime.now()
                logger.debug(f"Refresh done")

        logger.debug(f"Start refresh")
        Thread(target=refresh_thread_function).start()

    @property
    def human_ip(self):
        if self.ip is None:
            return "N/A"
        else:
            return self.ip

    @property
    def human_last_check(self):
        return humanize.naturaltime(self.last_check)

    @property
    def human_last_ping_ms(self):
        if self.last_ping_ms is None:
            return "∞"
        else:
            return f"{int(self.last_ping_ms)} ms"

    @property
    def human_mac(self):
        if self.mac is None:
            return "N/A"
        else:
            return self.mac

    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, value):
        logger.debug(f"Updating IP before lock")
        with RLock():
            logger.debug(f"Updating IP")
            self._ip = value

    @property
    def last_ping_ms(self):
        return self._last_ping_ms

    @last_ping_ms.setter
    def last_ping_ms(self, value):
        logger.debug(f"Updating ping before lock")
        with RLock():
            logger.debug(f"Updating ping")
            self._last_ping_ms = value

    @property
    def mac(self):
        return self._mac

    @mac.setter
    def mac(self, value):
        logger.debug(f"Updating MAC before lock")
        with RLock():
            logger.debug(f"Updating MAC")
            self._mac = value

    @property
    def status(self):
        if self.last_ping_ms is not None:
            return "up"
        else:
            return "down"

    def __repr__(self):
        return str(vars(self))


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    import time

    desktop = Device("nlandier-desktop")
    rpi01 = Device("rpi01")
    rpi02 = Device("rpi02")
    logger.info(rpi01)
    time.sleep(2)
    logger.info(desktop)
    logger.info(rpi01)
    logger.info(rpi02)
