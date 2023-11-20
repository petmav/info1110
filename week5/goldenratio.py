import sys

a = round(float(sys.argv[1]), 3)
b = round(float(sys.argv[2]), 3)

if (a + b / a) == 1.618:
    print('Golden ratio!')
else:
    print('Maybe next time.')