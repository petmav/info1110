print("Hello, welcome to Fresh Tomatoes! For a list of commands, enter 'help'. To exit, enter 'exit'.")

database = []

while True:
    inp = input()
    if inp == 'help':
        print(f'Enter the corresponding number to access that command.'
              f'1: Print all reviews'
              f'2: Choose a review by index and print the full review'
              f'3: Add a review'
              f'4: Delete a review')
    elif inp == 'exit':
        print('Exiting. Goodbye!')
        exit()
    elif inp == '':
        print('Sorry, empty input is not a valid command.')
    elif inp == '1':
        try:
            print(database)

    elif inp == '2':
        return
    elif inp == '3':
        return
    elif inp == '4':
        return
    else:
        print(f'Sorry, {inp} is not a valid command.')

