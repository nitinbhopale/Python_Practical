class vehicle:
    def __init__(self,color,cap,engpower,tyre):
        self.color=color
        self.capacity=cap
        self.enginpower=engpower
        self.tyre=tyre

    def start(self):
        pass

    def stop(self):
        pass

class car(vehicle):
    def __init__(self,airbags,gear,speed,fuel):
        self.Airbag=airbags
        self.gear=gear
        self.speed=speed
        self.fuel=fuel

    def accelerate