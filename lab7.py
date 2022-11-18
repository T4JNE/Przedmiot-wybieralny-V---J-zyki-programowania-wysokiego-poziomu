# (1) ==========================
import random

print("Zad 1")

a = 30
b = 78

print("a:", a)
print("b:", b)

c = a
a = b
b = c

print("a:", a)
print("b:", b)

# (2) ==========================
print("Zad 2")


def zamien(_a, _b):
    print("a:", _a)
    print("b:", _b)

    _c = _a
    _a = _b
    _b = _c


zamien(a, b)
print("a:", a)
print("b:", b)

# (3) ==========================
print("Zad 3")

def zamien(arr):
    print("a:", arr[0])
    print("b:", arr[1])

    _c = arr[0]
    arr[0] = arr[1]
    arr[1] = _c


arr = [a, b]
zamien(arr)
print("a:", arr[0])
print("b:", arr[1])

# (4) ==========================
print("Zad 4")


def odwroc(_arr):
    _arr = _arr.reverse()


print(arr)
odwroc(arr)
print(arr)

# (5) ==========================
print("Zad 5")


def sortuj(_arr):
    _arr = _arr.sort()


arr = []
for i in range(10):
    arr += [int(random.random() * 100)]

print(arr)
sortuj(arr)
print(arr)

arr = list("tekst tekst")
print(arr)
sortuj(arr)
print(arr)

# (6) ==========================
print("Zad 6")

arr = list(input())
sortuj(arr)
print(arr)

# (7) ==========================
print("Zad 7")

#Moze bedzie mi sie chcialo