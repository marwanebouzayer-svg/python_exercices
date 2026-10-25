from ex3 import Family
class TheIncredibles(Family):

    def use_power(self, name):
        for member in self.members:
            if member["name"] == name:
                if member["age"] > 18:
                    print(member["power"])
                else:
                    print("This member is not old enough to use their power")

    def incredible_presentation(self):
        print("Here is our powerful family")
        super().family_presentation()


members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male',
     'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},

    {'name': 'Sarah', 'age': 32, 'gender': 'Female',
     'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'}
]

my_family = TheIncredibles("Incredibles", members)

my_family.incredible_presentation()

my_family.born(
    name="Jack",
    age=1,
    gender="Male",
    is_child=True,
    power="Unknown Power",
    incredible_name="Baby Jack"
)

my_family.incredible_presentation()