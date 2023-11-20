line = input('Enter line: ')
an = input('Enter anagram: ')

def anagram(str1, str2):
    str1 = str1.lower()
    str1 = str1.replace('!', '')
    str2 = str2.lower()
    list1 = list(str1)
    list2 = list(str2)
    list1.sort()
    list2.sort()
    if list1 == list2:
        return f'Anagram!'
    else:
        return f'Not an anagram.'

x = anagram(line, an)
print()
print(x)