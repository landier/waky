import logging
import random
import time
from datetime import datetime, timedelta
from threading import Timer

from waky.core.device import Device

logger = logging.getLogger(__name__)

DEVICE_CHECK_PERIOD_IN_S = 60
INVENTORY_CHECK_THREAD_PERIOD_IN_S = 15


class Inventory:
    def __init__(self):
        self.devices = {}

    def run(self):
        def refresh_devices():
            logger.debug("Refresh devices")
            for device_key, device in self.devices.items():
                if device.last_check is None or datetime.now() - device.last_check >= timedelta(seconds=DEVICE_CHECK_PERIOD_IN_S):
                    logger.debug(f"Out of date device, refreshing: {device_key}")
                    device.refresh()
                    delay = random.uniform(0.5, 2.5)
                    logger.debug(f"Insert delay: {delay}")
                    time.sleep(delay)
            timer_thread = Timer(INVENTORY_CHECK_THREAD_PERIOD_IN_S, refresh_devices)
            timer_thread.daemon = True
            timer_thread.start()

        refresh_devices()

    def load(self, host_list):
        for host in host_list:
            self.devices[host] = Device(host)

    def __repr__(self):
        return str(vars(inventory))


if __name__ == "__main__":
    from waky.settings import devices

    inventory = Inventory()
    inventory.load(devices)
    inventory.run()
    print(inventory)
