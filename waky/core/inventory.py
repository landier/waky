from datetime import datetime, timedelta
from threading import Timer

from waky.core.device import Device


class Inventory:
    def __init__(self):
        self.devices = {}

    def run(self):
        def refresh_devices():
            timer_thread = Timer(15.0, refresh_devices)
            timer_thread.daemon = True
            timer_thread.start()
            for device in self.devices.values():
                if device.last_check is None or datetime.now() < device.last_check + timedelta(seconds=10):
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
