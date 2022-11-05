import math
#(1)
print("Zad 1")

str = input("Podaj tekst: ")
i=0

for char in str:
    i+=1

print(i)

#(1)
print("Zad 2")

str = input("Podaj tekst: ")
i=0

for char in str:
    if char=='a':
        i+=1

print(i)

#(3)
print("Zad 3")

str = input("Podaj tekst: ")
i=0
str+=' '

for char in str:
    if char==' ':
        i+=1
        print()
    else:
        print(char, end="")

print(i)

#(4)
print("Zad 4")

ln = 1
pi = 1
for i in range(2,10000,2):
    ln-=1/(i)
    ln+=1/(i+1)

print(ln)

for i in range(3,10000,4):
    pi-=1/(i)
    pi+=1/(i+2)
pi*=4

print(pi)

#(5)
print("Zad 5")

x = int(input("ile liczb?: "))
avg = 0

for i in range(x):
    avg += int(input())
avg /= x

print(avg)

#(6)
print("Zad 6")

for i in range(1, 21):
    print("sqrt: ", math.sqrt(i))
    print("sin: ", math.sin(i))

#(7)
print("Zad 7")

s = 1

for i in range(2,101):
    s += 1/(i**2)

print(math.sqrt(6 * s))

#(8)
print("Zad 8")
x = input()
print(x[::-1])

#(9)
print("Zad 9")
a = -1
b = 0

for i in range(100):
    c = (a+b)/2

    cc = c**5+c+1
    aa = a**5+a+1

    if (cc >= 0 and aa >= 0) or (cc < 0 and aa < 0):
        a = c
    else:
        b = c
print(c, cc)
