# 39. Slot Machine

import random

symbols = ['🍒', '🍇', '🍉', '7️⃣']
results = random.choices(symbols, k=3)

print(' | '.join(results))

if all(i == '7️⃣' for i in results):
    print("Jackpot! 💰")
else:
    print("Thanks for playing!")