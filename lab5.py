# (1) ==========================
import math

print("Zad 1")
l = [3, 'alfa', 2.71, 'kot']

print(l)
for i in range(-4,4):
    print("l[", i, "]: ", l[i])
print("=============")

l[0] = l[3]
l[3] = 'pies'

print(l)
print("=============")

l2 = l
print("l:", l)
print("l2:", l2)

l2[1] = 238

print("l:", l)
print("l2:", l2)

l3 = l.copy()
l3[0] = 'l3 najlepsze'

print("l:", l)
print("l3:", l3)

# (2) ==========================
print("Zad 2")
l = []

for i in range(1, 11):
    l += [i*i]
print(l)

for i in range(1, 11, 2):
    l[i] = -l[i]
print(l)

# (3) ==========================
print("Zad 3")
l = []

n = int(input("Podaj ilosc liczb: "))

for i in range(n):
    l += [input()]

print(l)
print("maksymalna wartosc: ", max(l))
print("minimalna wartosc: ", min(l))

# (4) ==========================
print("Zad 4")
l = []
n = int(input("Podaj n: "))

for i in range(1, n + 1):
    l += [math.sin(i)]

print("maksymalna wartosc: ", max(l))
print("minimalna wartosc: ", min(l))

# (5) ==========================
print("Zad 5")
l = []

for i in range(100,151):
    l += [i]

for i in range(len(l)-1, 0, -5):
    del l[i]
print(l)

# (6) ==========================
print("Zad 6")
l = []

for i in range(10):
    l += [i]

l2 = l[1: 10].copy()
l2 += [l[0]]
print("l: ",l)
print("l2: ",l2)

l3 = l[0: 9].copy()
l3.insert(0, l[9])
print("l3: ",l3)

l4 = l[::-1].copy()
print("l4: ",l4)

l5 = []
for i in range(10):
    if l[i]%2==0:
        l5 += [l[i]]
print("l5: ",l5)

l6 = []
for i in range(10):
    if i%2==0 and l[i]%2==1:
        l6 += [l[i]]

print("l6: ", l6)

# (7) ==========================
print("Zad 7")

l = []
pi = str(format(math.pi, '.50f'))

for i in range(2,52):
    l += [pi[i]]

print(l)