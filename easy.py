class Car:
    def __init__(self, speed, color, name, is_police: bool = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.sound = "BEEP"

    def go(self):
        print("Car is going")

    def stop(self):
        print("Car stopped")

    def direction(self, direction):
        print("Car turn ", direction)

    def carsound(self):
        print(self.sound)


class TownCar(Car):
    def __init__(self, speed, color, name, is_police: bool = False):
        super().__init__(speed, color, name, is_police)
        self.sound = "*Louder* BEEP"


class SportCar(Car):
    pass


class WorkCar(Car):
    def __init__(self, speed, color, name, is_pickup=True, is_police: bool = False):
        super().__init__(speed, color, name, is_police)
        self.is_pickup = is_pickup


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police: bool = True):
        super().__init__(self, speed, color, name, is_police)


car1 = TownCar(170, "Green", "Toyta")
car1.go()
car1.direction("right")
car1.stop()
car1.carsound()
