# Header file for the automobile class.

from headerclass.automobile import Automobile


def create_car(year: int, make: str, model: str, doors: int, roof: str) -> Automobile:
    return Automobile(year, make, model, doors, roof)
