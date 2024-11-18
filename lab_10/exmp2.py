def are_anagrams(word1, word2):
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()

    if sorted(word1) == sorted(word2):
        return "Anagrams"
    else:
        return "Not anagrams"


word1 = input("Введіть перше слово: ")
word2 = input("Введіть друге слово: ")

result = are_anagrams(word1, word2)
print(result)
