try:
    while True:
        inp = input()

        i = len(inp) - 1
        empty = ''

        while i > -1:
            empty = empty + inp[i]
            i = i - 1

        print(empty)

except EOFError:
    exit(1)