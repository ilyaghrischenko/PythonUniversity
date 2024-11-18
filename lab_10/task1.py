def check_hidden(word, combo):
    word = word.lower()
    combo = combo.lower()

    index = -1
    for char in word:
        index = combo.find(char, index + 1)
        if index == -1:
            return "No"
    return "Yes"


word = input("Введіть слово: ")
combo = input("Введіть комбінацію символів: ")

result = check_hidden(word, combo)
print(result)
