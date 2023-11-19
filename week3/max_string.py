print('Input 3 strings and find what string is the longest.')

string1 = input()
string2 = input()
string3 = input()

strings = [string1, string2, string3]

longest = max(strings, key=len)

if not len(strings[0]) == len(strings[1]) == len(strings[2]):
    print(f'{longest} is the longest string.')
else:
    if strings[0] == '' and strings[1] == '' and strings[2] == '':
        print('All strings are empty.')
    else:
        print('All strings are the same length.')

