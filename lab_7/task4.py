students = {
    "Іваненко": ("Іван", [90, 85, 92]),
    "Петренко": ("Петро", [80, 75, 88]),
    "Сидоренко": ("Сидір", [85, 95, 100]),
}

student_lastname = input("Введіть прізвище студента: ")

if student_lastname in students:
    name, grades = students[student_lastname]
    average = sum(grades) / len(grades)
    print(f"Ім'я: {name}, Оцінки: {grades}, Середній бал: {average:.2f}")
else:
    print("Студента не знайдено.")
