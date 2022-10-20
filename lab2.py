#(1)
print("Zad 1")
for i in range(5):
    print(i,end=" ")
print()

for i in range(4,8):
    print(i)
print()

for i in range(1,20,3):
    print(i)
print()

#(2)
print("Zad 2")
for i in range(2,22,2):
    print(i,end=" ")
for i in range(19,0,-2):
    print(i)
for i in range(1,11):
    print (i,"^ 2 =",i*i)

#(3)
print("Zad 3")
n=int(input("Wprowadz liczbę n: "))
m=int(input("Wprowadz liczbę m: "))
for i in range(n,m+1):
    print(i,end=" ")
for i in range(n,m-1,-1):
    print(i,end=" ")
print()

#(4)
print("Zad 4")
s=0
n=int(input("Podaj liczbę n: "))
for i in range(n):
    s=s+i
print(s)

#(5)
print("Zad 5")
n=0
w=0
while w < 1000000:
 w+=n
 n+=1
print("najmniejsze n to: ",n)

#(6)
print("Zad 6")
n=1
w=0
while w <10:
 w+=1/n
 n+=1
print("najmniejsze n spełniające warunek w zadaniu 6 to: ",n)

#(7)
print("Zad 7")
n=int(input("Podaj liczbę n: "))

i=1
while n>i:
    if i*i==n:
        print(n," jest kwadratem liczby: ",i)
        break
    i+=1

#(8)
print("Zad 8")
n=int(input("Podaj liczbę n: "))

for i in range(1,n):
    n*=i
print(n)

#(9)
print("Zad 9")
n=int(input("Podaj liczbę n: "))
m=int(input("Podaj liczbę m: "))
i=0
o=1
for i in range(m):
    o*=n
print(o)

#(10)
print("Zad 10")
n=int(input("Podaj liczbę n: "))

i=0
k=2
for i in range(2,n):
    if n%i==0:
        k+=1
print(k)

#(11)
print("Zad 11")


def is_prime(number):
    for i in range(2,number):
        if number%i==0:
            return False
    return True


n=int(input("Podaj liczbę n: "))

if is_prime(n):
    print(n, " to liczba pierwsza.")
else:
    print(n, " to liczba złożona.")

#(12)
print("Zad 12")
i=0
for i in range(1,201):
    if is_prime(i):
        print(i, end=" ")
print()
