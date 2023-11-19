import sys

first = sys.argv[1]
second = sys.argv[2]
val = False

if first > second:
    val = True
else:
    val = False

print(f'Is {first} > {second}? {val}')