import random

class MyList:
    def __init__(self, letters):
        self.letters = letters

    def reverse_list(self):
        return self.letters[::-1]

    def sort_list(self):
        return sorted(self.letters)

    def random_list(self):
        return [random.randint(1, 100) for i in range(len(self.letters))]


mylist = MyList(["d", "a", "c", "b"])

print("Reversed list:", mylist.reverse_list())
print("Sorted list:", mylist.sort_list())
print("Random list:", mylist.random_list())
