# ==========================
print("Zad 1")

t1 = (1, 5, 3, 7, 7)
t2 = (0, 1, 2, 3, 4)

print("t1:", t1)
print("t1 + t2:", t1 + t2)
print("t2 * 2:", t2 * 2)
print("len(t2):", len(t2))
print("max(t2):", max(t2))
print()

#t1[0] = 2 #generates error
print(t1)

l = list(t1)
l[0] = 2
t1 = tuple(l)
print(t1)

# ==========================
print("Zad 2")

l1 = ["Imie", "Nazwisko", "Wiek", 60, "Komentarz"]
l2 = ["Mariusz", "Pudzianowski", 45, False, "To by nic nie dalo"]

d = {}

for i in range(len(l1)):
    d[l1[i]] = l2[i]

print(d)

# ==========================
print("Zad 3")


def bezpowt(sl):
    _l = list(sl.values())

    for x in sl:
        if _l.count(sl[x]) > 1:
            return 0
    return 1


print(d)
if bezpowt(d):
    print("Nie ma powtorzen")
else:
    print("Sa powtorzenia")

print()

d = {"Imię": "Anna", "Wiek": 32, 5: "Costam", (6, 2): 32}
print(d)
if bezpowt(d):
    print("Nie ma powtorzen")
else:
    print("Sa powtorzenia")


# ==========================
print("Zad 4")


def odwr(sl):
    if not bezpowt(sl):
        print("Error, sa powtorzenia")
        return

    _d = {}
    for x in sl:
        _d[sl[x]] = x

    return _d


d = {"banana": "banan", "monkey": "malpa", "tree": "drzewo"}
print(d)
print(odwr(d))


# ==========================
print("Zad 5")

d = {"cat": "kot", "banana": "banan", "monkey": "malpa", "tree": "drzewo"}

fo = open('plik.txt', 'w')

for x in d:
    fo.write(str(d[x]) + ":" + str(x)+",")

fo.close()

# ==========================
print("Zad 6")

fo = open('plik.txt', 'r')

x = fo.read()

l = x.replace(",", ":").split(':')
l.pop()

d = {}
for i in range(0, len(l), 2):
    d[l[i]] = l[i+1]

print(d)

fo.close()
