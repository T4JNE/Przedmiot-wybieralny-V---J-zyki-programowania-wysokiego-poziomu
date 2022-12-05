import random
# ==========================
print("Zad 1")

fo = open('liczby.txt', 'w')

s = ""
for i in range(20):
    s += str(random.randint(1, 100)) + " "

fo.write(s)
fo.close()

# ==========================
print("Zad 2")

fo = open('liczby.txt', 'r')
numbers = []
s = ""

while True:
    ch = fo.read(1)

    if ch == "":
        break
    elif ch != " ":
        s += ch
    else:
        numbers += [int(s)]
        s = ""

print(numbers)
fo.close()

# ==========================
print("Zad 3")

fo = open('plik.txt', 'w')

for i in range(50):
    for j in range(50):
        if random.randint(1, 5) == 1:
            fo.write("*")
        else:
            fo.write(" ")
    fo.write("\n")

fo.close()

# ==========================
print("Zad 4")

fo = open('pierwsze.txt', 'w')

for num in range (2, 101):
    isprime = False
    for i in range(2, num):
        if num % i == 0:
            isprime = False
            break
        else:
            isprime = True

    if isprime:
        fo.write(str(num) + " ")

fo.close()

# ==========================
print("Zad 5")

fo = open('pierwsze.txt', 'r')

numbers = []
while True:
    ch = fo.read(1)

    if ch == "":
        break
    elif ch != " ":
        s += ch
    else:
        numbers += [int(s)]
        s = ""

last_prime = numbers[len(numbers)-1]
print(last_prime)

fo.close()

# ==

fo = open('pierwsze.txt', 'a')

for num in range (last_prime + 1, last_prime + 102):
    isprime = False
    for i in range(2, num):
        if num % i == 0:
            isprime = False
            break
        else:
            isprime = True

    if isprime:
        fo.write(str(num) + " ")

fo.close()

# ==========================
print("Zad 6")
