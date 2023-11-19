count = 1

while True:
    if count == 100:
        exit()
    elif count % 3 == 0 and count % 5 == 0:
        print('FizzBuzz')
    elif count % 5 == 0:
        print('Buzz')
    elif count % 3 == 0:
        print('Fizz')
    else:
        print(count)
    count += 1