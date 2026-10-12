family = {
    "rick": 43,
    "beth": 13,
    "morty": 5,
    "summer": 8
}

total_cost = 0

for name, age in family.items():
    if age < 3:
        price = 0
    elif age <= 12:
        price = 10
    else:
        price = 15

    print(name, "has to pay $", price)
    total_cost = total_cost + price

print("Total cost:", total_cost)