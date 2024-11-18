numbers = (10, 20, 5, 15, 30, 25)
n = int(input("Введіть число n: "))

result = [num for num in numbers if num < n]
print("Числа менші за", n, ":", result)
