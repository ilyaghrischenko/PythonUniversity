from random import randint

secret_number = randint(1, 10)

print("""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
|           (1 - 10)             |
+================================+
""")

while True:
    guess = int(input("Enter your guess: "))
    if guess == secret_number:
        print(f"{guess}\nWell done, muggle! Now you are free.")
        break
    else:
        print("Ha-ha! You're stuck in my loop!")
