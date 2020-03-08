from datetime import datetime, timedelta
from threading import Timer
import logging
from waky.core.device import Device


logger = logging.getLogger(__name__)


class Inventory:
    def __init__(self):
        self.devices = {}

    def run(self):
        def refresh_devices():
            timer_thread = Timer(15.0, refresh_devices)
            logger.debug("Refresh devices")
            timer_thread.daemon = True
            timer_thread.start()
            for device_key, device in self.devices.items():
                if device.last_check is None or datetime.now() < device.last_check + timedelta(seconds=10):
                    logger.debug(f"Out of date device, refreshing: {device_key}")
                    device.refresh()

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
