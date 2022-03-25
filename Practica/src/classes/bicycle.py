from src.classes.land import Land


class Bicycle(Land):
    def __init__(self, name, price, hasMotor, exerciseBike):
        super().__init__(name, price, hasMotor)
        self.exerciseBike = exerciseBike

    def displayData(self):
        print("Nombre: " + str(self.name) + " Precio:" + str(self.price) + " Tiene motor:" + str(self.hasMotor) + " Combustible: " + str(self.exerciseBike))
