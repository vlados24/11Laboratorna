from ua.lviv.iot.photographerDevice.models.PhotographerDevice import PhotographerDevice
from ua.lviv.iot.photographerDevice.models.Target import Target


class Lantern(PhotographerDevice):

    def __init__(self,

             weight=0.0, size=0.0, target=Target.SPORT_EVENT,
             colourTemperature=0.0, type="NoType"
             ):

        super(Lantern, self).__init__(
            weight, size, target
        )

        self.colourTemperature = colourTemperature
        self.type = type
