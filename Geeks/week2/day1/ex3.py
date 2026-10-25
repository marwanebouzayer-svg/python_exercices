class Family:
    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members

    def born(self, **kwargs):
        self.members.append(kwargs)
        print("Congratulations to the family!")

    def is_18(self, name):
        for member in self.members:
            if member["name"] == name:
                return member["age"] > 18
        return False

    def family_presentation(self):
        print("Family name:", self.last_name)

        for member in self.members:
            print(member)


members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
]

my_family = Family("Smith", members)

my_family.born(name="Jack", age=1, gender="Male", is_child=True)

print(my_family.is_18("Michael"))
print(my_family.is_18("Jack"))

my_family.family_presentation()