# (1) ==========================
print("Zad 1")

fo = open('plik.txt', 'w')
fo.write('To zostanie do dane do pliku!\nTo będzie w nowej linijce\n')
fo.close()

# (1) ==========================
print("Zad 2")

fo = open('plik.txt', 'r')
s = fo.read(5)
print(s)
s = fo.read(3)
print(s)
s = fo.read()
print(s)
fo.close()

fo = open('plik.txt', 'r')
while True:
    s = fo.read(3)
    if s == "":
        break
    print(s)
fo.close()

# (1) ==========================
print("Zad 3")

fo = open('plik.txt', 'a')
fo.writelines([input()+"\n", input()+"\n"])
fo.close()

# (1) ==========================
print("Zad 4")

fo = open('plik.txt', 'r')
s = fo.read()
print(s.count("a"))
fo.close()

# (1) ==========================
print("Zad 5")

fo = open('plik.txt', 'r')
i = 0
search_str = input()
while True:
    s = fo.readline()

    if s == "":
        break

    i += 1
    if s.find(search_str) != -1:
        print(i, end=". ")
        break
print(s)
fo.close()

# (1) ==========================
print("Zad 6")

fo = open('plik.txt', 'r')
file2 = open('plik2.txt', 'w')

s = fo.read()
file2.write(s.replace(" ", "*"))

fo.close()
file2.close()

# (1) ==========================
print("Zad 7")

fo = open('plik.txt', 'r')
file2 = open('plik3.txt', 'w')

s = fo.read()
file2.write(s.replace(" ", "*").upper())

fo.close()
file2.close()