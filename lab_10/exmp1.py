def is_palindrome(text):
    text = text.replace(" ", "").lower()

    if text == text[::-1]:
        return "It's a palindrome"
    else:
        return "It's not a palindrome"


text = input("Введіть текст: ")
result = is_palindrome(text)
print(result)
