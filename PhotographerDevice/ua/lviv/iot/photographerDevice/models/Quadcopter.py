from ua.lviv.iot.photographerDevice.models.PhotographerDevice import PhotographerDevice
from ua.lviv.iot.photographerDevice.models.Target import Target


class Quadcopter(PhotographerDevice):

    def __init__(self,

             weight=0.0, size=0.0, target=Target.SPORT_EVENT,
             maxHeight=0.0, power=0.0, batteryCapacity=0.0
             ):

        super(Quadcopter, self).__init__(
            weight, size, target
        )

        self.maxHeight = maxHeight
        self.power = power
        self.batteryCapacity = batteryCapacity
