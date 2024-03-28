# 40. Solar System

from math import pi
from random import choice as ch

planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]

random_panet = ch(planets)

if random_panet == 'Mercury':
    radius = 2440
elif random_panet == 'Venus':
    radius = 6052
elif random_panet == 'Earth':
    radius = 6371
elif random_panet == 'Mars':
    radius = 3390
elif random_panet == 'Saturn':
    radius = 58232
else:
    print('Oopsd! An error ocurred')

area = 4 * pi * (radius**2)
print(round(area, 2))