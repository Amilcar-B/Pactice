from src.classes.land import Land


class Car(Land):
    def __init__(self, name, price, hasMotor, useGas):
        super().__init__(name, price, hasMotor)
        self.useGas = useGas

    def displayData(self):
        print("Nombre: " + str(self.name) + " Precio:" + str(self.price) + " Tiene motor:" + str(self.hasMotor) + " Combustible: " + str(self.useGas))

