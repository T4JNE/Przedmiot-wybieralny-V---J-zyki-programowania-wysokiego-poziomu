'''
# (1) ==========================
print("Zad 1")

s = 'Ala ma kota'
lz = list(s)

for i in range(len(lz)):
    print(lz[i], end="")
print()

for i in lz:
    print(i, end="")
print()
# (2) ==========================
print("Zad 2")

print(lz.count('a'))

s = input()
lz = list(s)
print(lz.count('a'))
'''
# (3) ==========================
print("Zad 3")

num = 321
arr = list(str(num))
print(arr)

from math import factorial
print(factorial(6))

n = factorial(2000)
arr = list(str(n))
print(arr)

for i in range(10):
    print(i, ": ", arr.count(str(i)))


