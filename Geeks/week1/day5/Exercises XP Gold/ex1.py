import math

class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2

    def definition(self):
        print("A circle is a geometrical shape where all points")
        print("are at the same distance from the center.")


circle1 = Circle(5)

print("Perimeter:", circle1.perimeter())
print("Area:", circle1.area())
circle1.definition()