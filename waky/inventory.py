from waky.device import Device
from waky.settings import devices


class Inventory:
    def __init__(self):
        self.devices = {}
        pass

    def load(self, host_list):
        for host in host_list:
            self.devices[host] = Device(host)

    def __repr__(self):
        return str(vars(inventory))


if __name__ == "__main__":
    inventory = Inventory()
    inventory.load(devices)
    print(inventory)
