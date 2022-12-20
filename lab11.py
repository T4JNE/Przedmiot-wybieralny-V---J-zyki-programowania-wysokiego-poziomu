# ==========================
import random

print("Zad 1")
A = [[1, 2], [3, 4]]

for x in A:
    print(x)

# ==========================
print("Zad 2")


def zera(_a, _b):
    return [[0 for _ in range(_b)] for _ in range(_a)]


def id(_n):
    if _n <= 0:
        return 0

    _x = zera(_n, _n)

    for i in range(_n):
        for j in range(_n):
            if i == j:
                _x[i][j] = 1
    return _x


def wyswietl(_a):
    try:
        for _x in _a:
            print(_x)
    except TypeError:
        print(_a)


A = id(4)
wyswietl(A)

# ==========================
print("Zad 3")

def losowa(_a, _b, _n):
    _x = zera(_a, _b)

    for i in range(_a):
        for j in range(_b):
            _x[i][j] = random.randint(1, _n)
    return _x


def dodaj(_A, _B):
    if len(_A) != len(_B) or len(_A[0]) != len(_B[0]):
        return 0

    len_i = len(_A)
    len_j = len(_A[0])

    _x = zera(len(_A), len(_A[0]))

    for i in range(len_i):
        for j in range(len_j):
            _x[i][j] = _A[i][j] + _B[i][j]
    return _x

A = losowa(2, 3, 10)
B = losowa(2, 3, 10)
C = dodaj(A, B)
wyswietl(C)
# ==========================
print("Zad 4")


def pomnoz(_A, _B):
    return [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*_B)] for X_row in _A]


A = losowa(4, 7, 10)
B = losowa(2, 5, 10)
C = pomnoz(A, B)
wyswietl(C)
# ==========================
print("Zad 5")

def zamW(_A, _i, _j):
    _x = _A.copy()

    _t = _x[_i]
    _x[_i] = _x[_j]
    _x[_j] = _t

    return _x


def przemW(_A, _i, _k):
    _x = list(map(list, _A))

    for j in range(len(_x[_i])):
        _x[_i][j] = _x[_i][j] * _k

    return _x


def dodajW(_A, _i, _j, _k):
    _x = list(map(list, _A))

    for a in range(len(_x[_i])):
        for b in range(_k):
            _x[_i][a] += _x[_j][a]

    return _x

print("Przykladowa macierz A:")
A = losowa(4, 4, 10)
wyswietl(A)

print("\nPo zamianie wierza 4 z 2")
C = zamW(A, 3, 1)
wyswietl(C)

print("\nPo przemnozeniu wierza 4 5 razy")
C = przemW(A, 3, 5)
wyswietl(C)

print("\nPo dodaniu do wierza 1 wiersz 2 3 razy")
C = dodajW(A, 0, 1, 3)
wyswietl(C)

# ==========================
print("Zad 6")


def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]


def det(m):
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*det(getMatrixMinor(m,0,c))
    return determinant


A = losowa(3, 3, 15)
wyswietl(A)
print("Wyznacznik:", det(A))
