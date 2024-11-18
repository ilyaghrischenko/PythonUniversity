import math

x = 2.0
sigma = 1.0
mu = 0.0

gauss_value = (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-0.5 * ((x - mu) / sigma) ** 2)
print("Значення функції Гауса:", gauss_value)
