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

fo = open('plik6.txt', 'w')

Point1_x = random.randint(1, 50)
Point1_y = random.randint(1, 50)

Point2_x = random.randint(1, 50)
Point2_y = random.randint(1, 50)

#print(Point1_x, Point1_y)
#print(Point2_x, Point2_y)

for y in range(1, 51):
    for x in range(1, 51):
        line_equation = (Point2_x - Point1_x)*(y - Point1_y) - (Point2_y - Point1_y)*(x - Point1_x)

        #Odcinki start i koniec
        if (x == Point1_x and y == Point1_y) or (x == Point2_x and y == Point2_y):
            fo.write("*")
            #wyliczenie lini ze wzoru +-10    (Granice)
        elif abs(line_equation) <= 10 and (x > min(Point1_x, Point2_x) and x < max(Point1_x, Point2_x)):
            fo.write("*")
        else:
            fo.write(" ")
    fo.write("\n")

fo.close()

# ==========================
print("Zad 7")

fo = open('plik7.txt', 'w')

Point1_x = random.randint(2, 49)
Point1_y = random.randint(2, 49)
Radius = random.randint(1, max(min(50 - Point1_x, Point1_x, 50 - Point1_y, Point1_y), 1))

#print(Point1_x, Point1_y)
#print(Radius)

for y in range(1, 51):
    for x in range(1, 51):
        if abs((Point1_y-y)*(Point1_y-y)+(Point1_x-x)*(Point1_x-x) - (Radius * Radius)) <= Radius:
            fo.write("*")
        else:
            fo.write(" ")
    fo.write("\n")

fo.close()
