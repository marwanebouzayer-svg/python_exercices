my_list = [2, 3, 1, 2, "four", 42, 1, 5, 3, "imanumber"]

def sum_numbers(numbers):
    total = 0

    for number in numbers:
        try:
            total += number
        except TypeError:
            continue

    return total


print(sum_numbers(my_list))