my_list = list(map(int, input("Введіть елементи списку через пробіл: ").split()))

n = len(my_list)
for i in range(n):
    swapped = False
    for j in range(0, n - i - 1):
        if my_list[j] > my_list[j + 1]:
            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
            swapped = True
    if not swapped:
        break

print("Відсортований список:", my_list)
