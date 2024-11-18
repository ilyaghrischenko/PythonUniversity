def caesar_cipher(text, shift):
    result = []

    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            new_char = chr(base + (ord(char) - base + shift) % 26)
            result.append(new_char)
        else:
            result.append(char)

    return ''.join(result)


def get_valid_shift():
    while True:
        try:
            shift = int(input("Введіть значення зсуву (ціле число від 1 до 25): "))
            if 1 <= shift <= 25:
                return shift
            else:
                print("Зсув має бути в діапазоні від 1 до 25.")
        except ValueError:
            print("Будь ласка, введіть ціле число.")


text = input("Введіть рядок для шифрування: ")
shift = get_valid_shift()

encoded_text = caesar_cipher(text, shift)
print("Закодований текст:", encoded_text)
