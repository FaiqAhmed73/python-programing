class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def get_perameters(self):
        perimeter = self.a + self.b + self.c
        return perimeter

t1 = Triangle(3,4,5)


perimeter = t1.get_perameters()

print("The answer is", perimeter)