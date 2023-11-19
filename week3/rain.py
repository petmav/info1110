isRain = input('Is it currently raining? ')

if isRain == 'Yes':
    print('You should take the bus.')
elif isRain == 'No':
    kilometres = int(input('How far in km would you have to travel? '))
    if kilometres > 10:
        print('You should take the bus.')
    elif 1.99 < kilometres < 10.01:
        print('You should ride your bike.')
    else:
        print('You should walk.')
