import logging
import socket
import threading
from datetime import datetime

from ping3 import ping

FORMAT = "%(asctime)-15s %(id)s - %(message)s"
logging.basicConfig(level=logging.DEBUG, format=FORMAT)
logger = logging.getLogger("device")


class DeviceRefresher(threading.Thread):
    def __init__(self, device):
        self.device = device
        super().__init__()

    def run(self):
        try:
            ip = socket.gethostbyname(self.device.hostname)
            last_ping = ping(self.device.hostname, unit="ms", timeout=5)
        except socket.gaierror:
            logger.debug(f"Unknown host: {self.device.hostname}", extra={"id": threading.get_ident()})
        logger.debug(f"{ip} - {last_ping}", extra={"id": threading.get_ident()})
        self.device.refresh_callback(ip, last_ping)


class Device:
    def __init__(self, hostname):
        self.hostname = hostname
        self.ip = ""
        self.status = "down"
        self.last_ping = None
        self.last_check = None
        self.refresh()

    def refresh(self):
        refresher = DeviceRefresher(self)
        refresher.start()

    def refresh_callback(self, ip, last_ping):
        self.ip = ip
        self.last_ping = last_ping
        if last_ping is None:
            self.status = "down"
        else:
            self.status = "up"
        self.last_check = datetime.now()
        logger.debug(f"callback - {self.ip} - {self.last_ping}", extra={"id": threading.get_ident()})

    def __repr__(self):
        return str(vars(self))


if __name__ == "__main__":
    rpi01 = Device("rpi01")
    import time

    print(rpi01)
    time.sleep(2)
    print(rpi01)
