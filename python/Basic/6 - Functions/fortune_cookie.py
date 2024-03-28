# 29. Fortune Cookie

import random

def fortune():
    fortune = [
        "Don't pursue happiness – create it.",
        "All things are difficult before they are easy.",
        "The early bird gets the worm, but the second mouse gets the cheese.",
        "Someone in your life needs a letter from you.",
        "Don't just think. Act!",
        "Your heart will skip a beat.",
        "The fortune you search for is in another cookie.",
        "Help! I'm being held prisoner in a Chinese bakery!"
    ]

    num = random.randint(1, 8)\
    
    if num == 1:
        print(fortune[0])
    elif num == 2:
        print(fortune[1])
    elif num == 3:
        print(fortune[2])
    elif num == 4:
        print(fortune[3])
    elif num == 5:
        print(fortune[4])
    elif num == 6:
        print(fortune[5])
    elif num == 7:
        print(fortune[6])
    else :
        print(fortune[7])

for i in range(3):
    fortune()