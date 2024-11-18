def get_valid_input(prompt, min_val, max_val):
    while True:
        try:
            user_input = input(prompt)

            user_input = int(user_input)

            if min_val <= user_input <= max_val:
                return user_input
            else:
                print(f"Error: the value is not within permitted range ({min_val}..{max_val}).")
        except ValueError:
            print("Error: wrong input. Please enter a valid integer.")


num = get_valid_input("Введіть число від 1 до 10: ", 1, 10)
print(f"Ви ввели допустиме значення: {num}")
