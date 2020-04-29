import random
Roulette = random.randint(0, 36)
print("Spin resulted in" , Roulette, "...")
print("Pay", Roulette)
if Roulette in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]:
    print("Pay Red")
elif Roulette in [0, 00]:
    pass
else:
    print("Pay Black")
if Roulette % 2 == 1:
    print("Pay Odd")
elif Roulette * 5 == 0:
    pass
else:
    print("Pay Even")
if 19 > Roulette >= 1:
    print("Pay 1 to 18")
elif Roulette in [0, 00]:
    pass
else:
    print("Pay 19 to 36")