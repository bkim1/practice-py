import functools
arr = ['c', 'h', 'a', 'r', 'a', 'c', 't', 'e', 'r']

print("".join(arr))

for ch in arr:
    print(ch, sep='', end='')

print()

s = ""
for ch in arr:
    s += ch
print(s)

print(functools.reduce(lambda x, y: x + y, arr))