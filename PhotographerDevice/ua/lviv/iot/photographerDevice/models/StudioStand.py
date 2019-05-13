from ua.lviv.iot.photographerDevice.models.PhotographerDevice import PhotographerDevice
from ua.lviv.iot.photographerDevice.models.Target import Target


class StudioStand(PhotographerDevice):

    def __init__(self,

             weight=0.0, size=0.0, target=Target.SPORT_EVENT,
             lightSynchronizer="NoLightSynchronizer", maximumShootingHeight=0.0, minimumShootingHeight=0.0
             ):

        super(StudioStand, self).__init__(
            weight, size, target
        )

        self.lightSynchronizer = lightSynchronizer
        self.maximumShootingHeight = maximumShootingHeight
        self.minimumShootingHeight = minimumShootingHeight
