my_fav_numbers = {3, 7, 10}

my_fav_numbers.add(15)
my_fav_numbers.add(20)

my_fav_numbers.remove(20)

friend_fav_numbers = {5, 8, 12}

our_fav_numbers = my_fav_numbers | friend_fav_numbers

print(our_fav_numbers)