import sys

v1 = int(sys.argv[1])
v2 = int(sys.argv[2])
v3 = int(sys.argv[3])
u1 = int(sys.argv[4])
u2 = int(sys.argv[5])
u3 = int(sys.argv[6])

v = f'{{ {v1}, {v2}, {v3} }}'
u = f'{{ {u1}, {u2}, {u3} }}'
vdotu = (v1 * u1) + (v2 * u2) + (v3 * u3)
print(f'V = {v}')
print(f'U = {u}')
print(f'V . U = {vdotu}')

