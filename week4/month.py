import sys

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

inputMonth = int(sys.argv[1])
inputTime = int(sys.argv[2])

i = 0
month = months[inputMonth - 1]
finalMonth = inputMonth

while i < inputTime:
    if finalMonth % 12 == 0:
        finalMonth = inputMonth
    elif finalMonth >= 12:
        finalMonth = 0
    finalMonth += 1
    i += 1

final = months[(finalMonth - 1) % len(months)]

print(f"It's currently {month}, in {inputTime} months it will be {final}")



