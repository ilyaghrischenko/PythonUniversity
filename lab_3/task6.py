a = float(input("Введіть значення a: "))
b = float(input("Введіть значення b: "))

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b if b != 0 else "На нуль ділити не можна"

print("Сума:", addition)
print("Різниця:", subtraction)
print("Добуток:", multiplication)
print("Частка:", division)

print("\nThat's all, folks!")
