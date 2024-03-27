# 13. pH Levels
ph = int(input('Enter a pH value (0-14): '))

if ph > 7:
  print('Basic')
elif ph < 7:
  print('Acid')
else:
  print('Neutral')