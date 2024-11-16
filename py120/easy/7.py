class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_wheels(self):
        return 4

    def info(self):
        return f"{self.make} {self.model}"

class Motorcycle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_wheels(self):
        return 2

    def info(self):
        return f"{self.make} {self.model}"

class Truck:
    def __init__(self, make, model, payload):
        self.make = make
        self.model = model
        self.payload = payload

    def get_wheels(self):
        return 6

    def info(self):
        return f"{self.make} {self.model}"