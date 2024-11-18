hat_list = [1, 2, 3, 4, 5]

hat_list[len(hat_list) // 2] = int(input("Введіть ціле число для заміни середнього елемента: "))

hat_list.pop()

print("Довжина списку:", len(hat_list))
print("Оновлений список:", hat_list)
