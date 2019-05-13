import sys
sys.path.insert(0, '../models')
from ua.lviv.iot.photographerDevice.models.Target import Target
from ua.lviv.iot.photographerDevice.models.Camera import Camera
from ua.lviv.iot.photographerDevice.models.Lantern import Lantern
from ua.lviv.iot.photographerDevice.models.PhotographerDevice import PhotographerDevice
from ua.lviv.iot.photographerDevice.models.Quadcopter import Quadcopter
from ua.lviv.iot.photographerDevice.models.StudioStand import StudioStand


class PhotographerDeviceManager:
    def __init__(self, *args):
        self.devices = args

    @staticmethod
    def sortBySize(devices, descending=False):
        return sorted(devices, key=lambda device: device.size, reverse=descending)

    @staticmethod
    def sortBySizeAscending(devices):
        return PhotographerDeviceManager.sortBySize(devices)

    @staticmethod
    def sortBySizeDescending(devices):
        return PhotographerDeviceManager.sortBySize(devices, True)

    @staticmethod
    def sortByWeight(devices, descending=False):
        return sorted(devices, key=lambda device: device.weight, reverse=descending)

    @staticmethod
    def sortByWeightAscending(devices):
        return PhotographerDeviceManager.sortByWeight(devices)

    @staticmethod
    def sortByWeightDescending(devices):
        return PhotographerDeviceManager.sortByWeight(devices, True)

    def filterByTarget(self, target):
        return list(filter(lambda device: device.target == target, self.devices))


def main():
    devices = [
        PhotographerDevice(20, 10, Target.SPORT_EVENT),
        Camera(10, 20, Target.CLASSIC_EVENT, "Sony", "SuperDisplay", 2, "Best"),
        Lantern(30, 30, Target.LANDSCAPE, 2, "Cool"),
        Quadcopter(40, 50, Target.SPORT_EVENT, 20, 10, 30),
        StudioStand(50, 40, Target.LANDSCAPE, "Black", 10, 20)
    ]
    manager = PhotographerDeviceManager(*devices)

    filteredList = manager.filterByTarget(0)
    for s in filteredList:
        print(s)
    print()

    sortedList = PhotographerDeviceManager.sortBySizeAscending(devices)
    for s in sortedList:
        print(s)
    print()

    sortedFilteredList = PhotographerDeviceManager.sortByWeightDescending(filteredList)
    for s in sortedFilteredList:
        print(s)


if __name__ == '__main__':
    main()