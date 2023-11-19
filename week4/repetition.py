import sys

words = ['one', 'one', 'one']

i = 0
rep = 0

while i < len(words):
    j = 1
    while j < len(words):
        if words[i] == words[j] and i != j:
            rep += 1
        j += 1
    i += 1

print(rep)
