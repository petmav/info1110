import sys

try:
    attempts = int(sys.argv[1])

except ValueError:
    print('Invalid arguments.')
    exit()

if attempts < 0:
    print('Invalid arguments.')
    exit()

password = sys.argv[2]

i = 0
attemptCount = 1

while i < attempts:
    login = input(f'Enter password (attempt {attemptCount} of {attempts}): ')
    if login == password:
        print('Password accepted! Welcome!')
    else:
        print('Incorrect password.')
        attemptCount += 1
    i += 1
