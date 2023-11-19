inp = input()

countzero = 0
countone = 0
counttwo = 0
countthree = 0
countfour = 0
countfive = 0
countsix = 0
countseven = 0
counteight = 0
countnine = 0

i = 0

while i < len(inp):
    if inp[i] == '0':
        countzero += 1
    if inp[i] == '1':
        countone += 1
    if inp[i] == '2':
        counttwo += 1
    if inp[i] == '3':
        countthree += 1
    if inp[i] == '4':
        countfour += 1
    if inp[i] == '5':
        countfive += 1
    if inp[i] == '6':
        countsix += 1
    if inp[i] == '7':
        countseven += 1
    if inp[i] == '8':
        counteight += 1
    if inp[i] == '9':
        countnine += 1
    i += 1

print(f'0: {countzero}')
print(f'1: {countone}')
print(f'2: {counttwo}')
print(f'3: {countthree}')
print(f'4: {countfour}')
print(f'5: {countfive}')
print(f'6: {countsix}')
print(f'7: {countseven}')
print(f'8: {counteight}')
print(f'9: {countnine}')


