from src.classes.transport import Transport


class Land(Transport):
    def __init__(self, name, price, hasMotor):
        super().__init__(name, price)
        self.hasMotor = hasMotor

    def displayData(self):
        print("Nombre: " + str(self.name) + " Precio:" + str(self.price) + " Tiene motor:" + str(self.hasMotor))