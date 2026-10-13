word = input("Enter a word: ")

result = word[0]

for i in range(1, len(word)):
    if word[i] != word[i - 1]:
        result += word[i]

print(result)


