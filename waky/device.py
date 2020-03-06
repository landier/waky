import logging
import socket
import threading
from datetime import datetime

from ping3 import ping

FORMAT = "%(asctime)-15s %(id)s - %(message)s"
logging.basicConfig(level=logging.DEBUG, format=FORMAT)
logger = logging.getLogger("device")


class Device:
    def __init__(self, hostname):
        self.hostname = hostname
        self.ip = ""
        self.status = "down"
        self.last_ping = None
        self.last_check = None
        self.refresh()

    def refresh(self):
        try:
            self.ip = socket.gethostbyname(self.hostname)
            self.last_ping = ping(self.hostname, unit="ms", timeout=5)
            if self.last_ping is None:
                self.status = "down"
            else:
                self.status = "up"
        except socket.gaierror:
            logger.debug(f"Unknown host: {self.hostname}", extra={"id": threading.get_ident()})
            self.status = "down"
        self.last_check = datetime.now()
        logger.debug(self, extra={"id": threading.get_ident()})

    def __repr__(self):
        return str(vars(self))


if __name__ == "__main__":
    rpi01 = Device("rpi01")
    print(rpi01)
