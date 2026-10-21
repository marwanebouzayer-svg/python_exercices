import math


class Circle:

    def __init__(self, radius=None, diameter=None):

        if radius is not None:
            self.radius = radius

        elif diameter is not None:
            self.radius = diameter / 2

        else:
            self.radius = 0

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle with radius: {self.radius}, diameter: {self.diameter}, area: {self.area:.2f}"

    def __add__(self, other):
        return Circle(radius=self.radius + other.radius)

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius


# Create circles
circle1 = Circle(radius=5)
circle2 = Circle(diameter=20)
circle3 = Circle(radius=3)
circle4 = Circle(radius=5)

# Print circles
print("Circle 1:", circle1)
print("Circle 2:", circle2)

# Area
print("\nArea:", circle1.area)

# Addition
circle5 = circle1 + circle2
print("\nAddition:", circle5)

# Comparison
print("\nCircle 1 < Circle 2:", circle1 < circle2)
print("Circle 1 == Circle 4:", circle1 == circle4)

# Sorting
circles = [circle1, circle2, circle3, circle4]

circles.sort()

print("\nSorted circles:")

for circle in circles:
    print(circle)