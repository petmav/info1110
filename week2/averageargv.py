import sys

floats = [float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5])]

average = (floats[0] + floats[1] + floats[2] + floats[3] + floats[4]) / 5

print(f'Average is {float(average):.2f}')