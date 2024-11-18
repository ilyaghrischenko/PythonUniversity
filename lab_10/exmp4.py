while True:
    try:
        number = int(input("Введіть ціле число: "))

        print(6 / number)
        break
    except ValueError:
        print("Введене значення не є допустимим числом. Повторіть спробу...")
    except ZeroDivisionError:
        print("Не можна поділити на нуль. Повторіть спробу...")
