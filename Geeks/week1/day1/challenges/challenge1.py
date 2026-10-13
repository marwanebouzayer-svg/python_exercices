number = int(input("Enter a number: "))
length = int(input("Enter the length: "))

result = []

for i in range(1, length + 1):
    result.append(number * i)

print(result)