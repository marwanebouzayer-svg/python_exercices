import random

number = int(input("Enter a number between 1 and 100: "))

if number >= 1 and number <= 100:
    random_number = random.randint(1, 100)

    if number == random_number:
        print("Success!")
    else:
        print("Fail!")
        print("Your number:", number)
        print("Random number:", random_number)
else:
    print("Invalid number")