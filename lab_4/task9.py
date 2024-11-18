user_word = input("Enter a word: ").upper()

for letter in user_word:
    if letter in "AEIOU":
        continue
    print(letter)
