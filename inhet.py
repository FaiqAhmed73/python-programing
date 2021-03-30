class Vehicle:
    def __init__(self, color):
        self.color = color

    def col(self):
        print("color")

    def get_perameters(self):
        colo1 = self.color
        return colo1


class Car(Vehicle):
    def my_car(self):
        print("i am Car")

class MotorCycle(Vehicle):
    def my_motorcycle(self):
        print("i am motor cycle")

necarcol = Car("blue")
nemotcol = MotorCycle("white")

c1 = necarcol.get_perameters()

m1 = nemotcol.get_perameters()

print("thie color is", c1)
print("thie color is", m1)



    