# 33. Drive-Thru

def welcome():
  print("WELCOME TO MC DONALDS")
  print("\n")
  print("MENU:")
  print("   1) 🍔 Cheeseburger")
  print("   2) 🍟 Fries")
  print("   3) 🥤 Soda")
  print("   4) 🍦 Ice Cream")
  print("   5) 🍪 Cookie")
  print("\n")

def get_item(number):
  if number == 1:
    return '🍔 Cheeseburger'
  elif number == 2:
    return '🍟 Fries'
  elif number == 3:
    return '🥤 Soda'
  elif number == 4:
    return '🍦 Ice Cream'
  elif number == 5:
    return '🍪 Cookie'
  else:
    return 'Invalid option'



welcome()
option = int(input('What would you like to order? '))
print(get_item(option))