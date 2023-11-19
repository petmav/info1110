from random import *

seed(1)

luckValue = randint(0, 100)
luckBoost = 0

lucky = input('Feeling lucky today? (y/n) ')

if lucky not in ['y', 'n']:
    print('Invalid input :(')
elif lucky == 'n':
    luckBoost = int(input('How much do you want to boost your luck? '))
    if luckBoost < 0:
        print('Invalid input :(')
        exit()
    else:
        print(f'You are {(luckValue + luckBoost) % 100}% lucky today. Goodbye!')
else:
    print(f'You are {(luckValue + luckBoost) % 100}% lucky today. Goodbye!')

