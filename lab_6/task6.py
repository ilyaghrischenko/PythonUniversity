def is_a_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

print(is_a_triangle(3, 4, 5))  # True
print(is_a_triangle(1, 1, 2))  # False
