#(3)
print("Zad 3")
for i in range(10):
    for j in range(10):
        print("*", end=" ")
    print()

#(4)
print("Zad 4")
for i in range(10):
    for j in range(10):
        if i==0 or i==9 or j==0 or j==9:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#(5)
print("Zad 5")
for i in range(10):
    for j in range(10):
        #  [Obramowanie kwadratu]    [przekatna 1][przekatna 2]
        if i==0 or i==9 or j==0 or j==9 or i==j or i+j==9:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#(6)
print("Zad 6")
for i in range(10):
    for j in range(10):
        if (i+j)%2==0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#(7)
print("Zad 7")
for i in range(1,11):
    for j in range(1,11):
        if(i*j<10):
            print(i*j," ", end="")
        else:
            print(i*j, end=" ")
    print()

#(8)
print("Zad 8")
for i in range(10):
    for j in range(10):
        if i<=j-5 or i>=j+5 or i+j>=9+5 or i+j<=9-5:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#(9)
print("Zad 9")
for i in range(1,11):
    for j in range(1,11):
        if i==1 or j==1:
            print(i*j, end=" ")
        elif i**j<j**i:
            print("<", end=" ")
        elif i**j>j**i:
            print(">", end=" ")
        else:
            print("=", end=" ")
    print()

#(10)
print("Zad 10")
for i in range(1,10):
    for j in range(1,10):
        if (5-i)*(5-i)+(5-j)*(5-j)<=18:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
