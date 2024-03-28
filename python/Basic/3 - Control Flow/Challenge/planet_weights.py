# Planet Weights
# Create a weight conversion program that:
#   Asks the user what their Earth weight is (as a float).
#   Asks the user for a planet number (as an int).
# To calculate the user's weight:
# destination weight = Earth weight × relative gravity

# Write code below 💖

earth_weight = float(input('Enter your weight: '))
print('PLANETS: ')
print(' 1) Mercury')
print(' 2) Venus')
print(' 3) Mars')
print(' 4) Jupiter')
print(' 5) Saturn')
print(' 6) Uranus')
print(' 7) Neptune')
planet = int(input('Enter the planet number: '))

if planet == 1:
  destination_weight = earth_weight*0.38
  print(destination_weight)
elif planet == 2:
  destination_weight = earth_weight*0.91
  print(destination_weight)
elif planet == 3:
  destination_weight = earth_weight*0.38
  print(destination_weight)
elif planet == 4:
  destination_weight = earth_weight*2.53
  print(destination_weight)
elif planet == 5:
  destination_weight = earth_weight*1.07
  print(destination_weight)
elif planet == 6:
  destination_weight = earth_weight*0.89
  print(destination_weight)
elif planet == 7:
  destination_weight = earth_weight*1.14
  print(destination_weight)
else:
  print('Invalid planet number')
