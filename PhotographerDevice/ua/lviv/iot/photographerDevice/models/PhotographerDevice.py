from ua.lviv.iot.photographerDevice.models.Target import Target


class PhotographerDevice:

    def __init__(self,
                 weight=0.0, size=0.0, target=Target.SPORT_EVENT):

        self.weight = weight
        self.size = size
        self.target = target



    def __str__(self):

        return ', '.join((f"{name} = {value}" for name, value in self.__dict__.items()))