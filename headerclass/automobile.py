# This is the main file for the headerclass.


class Vehicle:
    def __init__(self, vehicle_type: str) -> None:
        self.vehicle_type = vehicle_type


class Automobile(Vehicle):
    def __init__(
        self,
        year: int,
        make: str,
        model: str,
        doors: int,
        roof: str,
    ) -> None:
        super().__init__("Automobile")
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

