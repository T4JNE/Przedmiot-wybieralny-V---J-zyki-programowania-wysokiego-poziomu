
#(1)
print("Zad 1")
a = 2
b = 5
c = 5.0
d = 4.2
print(a, b, c, d)

#(2)
print("Zad 2")
s = "kot"
t = "pies"
print(s, t)

#(3)
print("Zad 3")
i = input("Podaj i ")
j = input("Podaj j ")
print(i,j,i+j)

#(4)
print("Zad 4")
i = int(float(input("Podaj i ")))
print (i)

#(5)
print("Zad 5")
i = int(input("Podaj i "))
j = int(input("Podaj j "))
print("%", i%j)
print("//", i//j)

#(6)
print("Zad 6")
a = int(input("Podaj a "))
b = int(input("Podaj b "))
c = int(input("Podaj b "))

if(a>10):
    print(a)
if(b>10):
    print(b)
if(c>10):
    print(c)

#(7)
print("Zad 7")
a = int(input("Podaj a "))

if(a%2==0):
    print("Parzysta")
else:
    print("Nieparzysta")

#(8)
print("Zad 8")
a = int(input("Podaj rok "))

if(a%4==0 or (a%100==0 and a%400==0)):
    print("Przestepny")
else:
    print("Nie przestepny")

#(9)
print("Zad 9")
a = float(input("Podaj liczbe "))
print(int(a)%10, int((a*10)%10))

#(10)
print("Zad 10")
a = float(input("Podaj liczbe 1 "))
b = float(input("Podaj liczbe 2 "))

a_decimal = a - int(a)
b_decimal = b - int(b)

a = int(a) + b_decimal
b = int(b) + a_decimal

print(a,b)

#(11)
print("Zad 11")
i = float(input("Podaj liczbe i "))
j = float(input("Podaj liczbe j "))

i_pow = i**j
j_pow = j**i

if(i_pow>j_pow):
    print(i, "do", j, "równe", i_pow, "jest większe od", j, "do", i, "równe", j_pow,)
elif(i_pow<j_pow):
    print(i, "do", j, "równe", i_pow, "jest mniejsze od", j, "do", i, "równe", j_pow,)
else:
    print(i, "do", j, "równe", i_pow, "jest równe", j, "do", i, "równe", j_pow,)

#(12)
print("Zad 12")
a = float(input("Podaj liczbe pod pierwiastkiem "))
b = float(input("Podaj stopien pierwiastka "))

print(a**(1/b))
