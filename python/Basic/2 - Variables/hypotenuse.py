# 09. Pythagoreanm Theorem
# Write code below 💖
import math
import cmath

a = int(input('Enter a: '))
b = int(input('Enter b: '))

c = math.sqrt((a**2) + (b**2))

print(c)

# BONUS: Quadratic Formula
a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

x1 =((-b) + cmath.sqrt(b**2 - 4*a*c))/2*a
x2 =((-b) - cmath.sqrt(b**2 - 4*a*c))/2*a

print(x1)
print(x2)