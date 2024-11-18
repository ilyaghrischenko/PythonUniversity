while True:
    try:
        num = int(input("Введіть ціле число: "))
        print(6 / num)
        break
    except ValueError:
        print("Введене значення не є допустимим числом. Повторіть спробу...")
    except ZeroDivisionError:
        print("Не можна поділити на нуль. Повторіть спробу...")
