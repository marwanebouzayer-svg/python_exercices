class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight:
            return f"{self.name} wins the fight"
        elif self.run_speed() * self.weight < other_dog.run_speed() * other_dog.weight:
            return f"{other_dog.name} wins the fight"
        else:
            return "It's a draw"


dog1 = Dog("Rex", 3, 20)
dog2 = Dog("Max", 2, 15)
dog3 = Dog("Rocky", 4, 25)

print(dog1.bark())
print(dog2.run_speed())

print(dog1.fight(dog2))
print(dog2.fight(dog3))