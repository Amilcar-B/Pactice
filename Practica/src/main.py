from src.classes.bicycle import Bicycle
from src.classes.car import Car
from src.classes.land import Land
from src.classes.transport import Transport

if __name__ == "__main__":
    land1: Transport = Bicycle("b", 100, False, True)
    land2: Transport = Car("c", 50, True, False)
    land3: Transport = Land("d", 70, False)

    landList = [land1, land2, land3]

    for transport in landList:
        transport.displayData()

