# Create a calculator.py program that calculates the area of one of the following shapes:
#   1. Square
#   2. Rectangle
#   3. Triangle
#   4. Circle
# The program should present a menu for the user to choose which shape to calculate, then ask them for the appropriate values (side, length, width, etc.).

# Then, it should calculate the area and print it out.
#
# Autor: Carmen Chunyin Fernandez Nuñez
# Alias: Alissea

import math

print("==================")
print("Area Calculator 📐")
print("==================")
print("\n")

quit = False

while quit == False:
    area = 0
    print(' 1) Triangle')
    print(' 2) Rectangle')
    print(' 3) Square')
    print(' 4) Circle')
    print(' 5) Quit')
    print("\n")
    figure = int(input('Which shape: '))
    print("\n")

    if figure == 1: # Triangle
        base = int(input('Base: '))
        height = int(input('Height: '))
        area = (base * height) / 2
        
    
    elif figure == 2: # Rectangle
        lenght = int(input('Lenght: '))
        widht = int(input('Widht: '))
        area = lenght * widht

    elif figure == 3: # Square
        side = int(input("Side: "))
        area = side**2
    
    elif figure == 4: # Circle
        radius = int(input('Radius: '))
        area = math.pi * (radius**2)
    
    elif figure == 5:
        quit = True
    
    else:
        print("Option not valid\n")
    
    if figure != 5:
        print("\n")
        print(f'The area is {area}\n')
    
    else:
        print("==================")
        print("Closing Program...")
        print("==================")
        print("\n")
