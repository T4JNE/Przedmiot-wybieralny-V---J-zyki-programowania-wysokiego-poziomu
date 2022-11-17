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

# (3) ==========================
print("Zad 3")

num = 321
arr = list(str(num))
print(arr)
'''
from math import factorial

print(factorial(6))
'''
n = factorial(1000)
arr = list(str(n))
print(arr)

for i in range(10):
    print(i, ": ", arr.count(str(i)))

# (4) ==========================
print("Zad 4")

arr = []
for i in range(31):
    arr.append(3**i - 2**i)
print(arr)

i = arr.index(1161737179)
print("arr[", i, "]:", arr[i])

# (5) ==========================
print("Zad 5")

arr2 = []

for i in arr:
    arr2 += [i % 19]

n = int(input())
x = 0
print(arr2)

if(n in arr2):
    for i in arr2:
        if i == n:
            x += 1
    print("podana liczba wystepuje", x, "razy")
else:
    print("podana liczba nie wystepuje")
'''
# (6) ==========================
print("Zad 6")

arr = []
for i in range(1, 101):
    arr += [1 / i]

print("suma:", sum(arr))
print("minimum:", min(arr))
print("maximum:", max(arr))

n = factorial(1000)
arr = list(str(n))

for i in range(len(arr)):
    arr[i] = int(arr[i])

print("suma cyfr 1000!: ", sum(arr))

# (7) ==========================
print("Zad 7")

'''
Nie rozumiem polecenia

def occurs_times(l, number):
    output = 0
    if (number in l):
        for i in l:
            if i == n:
                output += 1

    return output

for i in range(10,100):
    print(i, "wystepuje", occurs_times(arr, i), "razy")
'''