class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


cat1 = Cat("Tom", 3)
cat2 = Cat("Mimi", 7)
cat3 = Cat("Simba", 5)


def find_oldest_cat(cat1, cat2, cat3):
    if cat1.age > cat2.age and cat1.age > cat3.age:
        return cat1
    elif cat2.age > cat1.age and cat2.age > cat3.age:
        return cat2
    else:
        return cat3


oldest_cat = find_oldest_cat(cat1, cat2, cat3)

print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")
