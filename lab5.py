# (1) ==========================
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

