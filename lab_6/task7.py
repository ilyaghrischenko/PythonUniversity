from task6 import is_a_triangle

def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    sides = sorted([a, b, c])
    return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2

print(is_a_right_triangle(3, 4, 5))  # True
print(is_a_right_triangle(5, 12, 13))  # True
print(is_a_right_triangle(1, 2, 3))  # False
