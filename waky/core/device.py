import logging
import socket
from datetime import datetime
from threading import RLock, Thread

from ping3 import ping


logger = logging.getLogger(__name__)


class Device:
    def __init__(self, hostname):
        self.hostname = hostname
        self.ip = None
        self.last_ping = None
        self.last_check = None
        self.refresh()

    def refresh(self):
        def refresh_thread_function():
            try:
                self.ip = socket.gethostbyname(self.hostname)
                self.last_ping = ping(self.hostname, unit="ms", timeout=5)
            except socket.gaierror:
                logger.debug(f"Unknown host")
            finally:
                self.last_check = datetime.now()
                logger.debug(f"Refresh done")

        logger.debug(f"Start refresh")
        Thread(target=refresh_thread_function).start()

    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, value):
        logger.debug(f"Updating ip before lock")
        with RLock():
            logger.debug(f"Updating ip")
            self._ip = value

    @property
    def last_ping(self):
        return self._last_ping

    @last_ping.setter
    def last_ping(self, value):
        logger.debug(f"Updating ping before lock")
        with RLock():
            logger.debug(f"Updating ping")
            self._last_ping = value

    @property
    def status(self):
        if self.last_ping is not None:
            return "up"
        else:
            return "down"

    def __repr__(self):
        return str(vars(self))


if __name__ == "__main__":
    import time

    rpi01 = Device("rpi01")
    rpi02 = Device("rpi02")
    logger.info(rpi01, extra={"hostname": rpi01.hostname})
    time.sleep(2)
    logger.info(rpi01, extra={"hostname": rpi01.hostname})
    logger.info(rpi02, extra={"hostname": rpi02.hostname})
