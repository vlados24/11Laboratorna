from ua.lviv.iot.photographerDevice.models.PhotographerDevice import PhotographerDevice
from ua.lviv.iot.photographerDevice.models.Target import Target


class Camera(PhotographerDevice):

    def __init__(self,

             weight=0.0, size=0.0, target=Target.SPORT_EVENT,
             model="NoModel", rotaryDisplay="NoRotaryDisplay", matrix=0.0, processor="NoProcessor"
             ):

        super(Camera, self).__init__(
            weight, size, target
        )

        self.model = model
        self.rotaryDisplay = rotaryDisplay
        self.matrix = matrix
        self.processor = processor