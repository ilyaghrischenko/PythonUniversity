library = {
    "1984": ("Джордж Орвелл", 1949, 328),
    "До світла": ("Джек Лондон", 1907, 240),
    "Майстер і Маргарита": ("Михайло Булгаков", 1966, 512),
}

book = input("Введіть назву книги: ")

if book in library:
    author, year, pages = library[book]
    print(f"Автор: {author}, Рік видання: {year}, Кількість сторінок: {pages}")
else:
    print("Книга не знайдена.")
