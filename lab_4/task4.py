income = float(input("Enter the annual income: "))

if income <= 85528:
    tax = income * 0.18 - 556.02
else:
    tax = 14839.02 + 0.32 * (income - 85528)

tax = max(0, round(tax, 0))
print(f"The tax is: {tax} thalers")
