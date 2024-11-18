def life_path_number(birthdate):
    digits = ''.join(filter(str.isdigit, birthdate))

    while len(digits) > 1:
        digits = str(sum(int(digit) for digit in digits))

    return digits


birthdate = input("Введіть дату народження у форматі YYYYMMDD: ")
result = life_path_number(birthdate)
print(result)
