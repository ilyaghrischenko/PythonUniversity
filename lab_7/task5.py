phone_book = {
    "Олександр": ["+380501234567", "+380987654321"],
    "Марія": ["+380671234567"],
    "Дмитро": ["+380931234567", "+380501112233"],
}

def add_phone(contact_name, phone_number):
    if contact_name in phone_book:
        phone_book[contact_name].append(phone_number)
    else:
        phone_book[contact_name] = [phone_number]

name = input("Введіть ім'я контакту: ")
number = input("Введіть новий номер телефону: ")
add_phone(name, number)

print("Телефонна книга:")
for contact, numbers in phone_book.items():
    print(contact, ":", ", ".join(numbers))
