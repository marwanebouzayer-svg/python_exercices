class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")


davids_dog = Dog("Rex", 50)

print("David's dog:", davids_dog.name)
print("Height:", davids_dog.height, "cm")
davids_dog.bark()
davids_dog.jump()


sarahs_dog = Dog("Teacup", 20)

print("Sarah's dog:", sarahs_dog.name)
print("Height:", sarahs_dog.height, "cm")
sarahs_dog.bark()
sarahs_dog.jump()


if davids_dog.height > sarahs_dog.height:
    print("The bigger dog is", davids_dog.name)
elif sarahs_dog.height > davids_dog.height:
    print("The bigger dog is", sarahs_dog.name)
else:
    print("Both dogs have the same height.")