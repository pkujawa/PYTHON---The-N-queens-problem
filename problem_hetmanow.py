import random


n = int(input("Podaj dlugosc boku szachownicy"))
#rysowanie szachownicy o wymierach nxn

# x to lista kolumn, gdzie x[i] to numer wierwsza
x = n * [None]
# lista wierszy - szachowanie w poziomie - jeśli True, to znaczy że nie ma szacha
a = n * [True]

# lista przekątnych \ - jest ich 2n-1 - True oznacza brak szacha
b = (2*n-1) * [True]

# lista przekątnych / Różnica wiersz-kolumna od (-N+1) do (N-1).  
c = (2*n-1) * [True]
lista = []

def dodaj_hetmana(col):
    global lista
    for row in range(n):
        if sprawdz(row, col):
            zapisz(row, col)
            if col < (n-1):
                dodaj_hetmana(col+1)
            else:
                lista.append([z for z in x])
                print(x)
                print(lista)
                rysuj_szachownice()
                # self.lista.append(self.x)
            wymaz(row, col)

def sprawdz(row, col):
    return a[row] and b[row+col] and c[row-col]

def zapisz(row, col):
    x[col] = row
    a[row] = False
    b[row+col] = False
    c[row-col] = False


def wymaz(row, col):
    a[row] = True
    b[row+col] = True
    c[row-col] = True

def rysuj_szachownice():
    print(x)
    # print(self.lista)
    for row in range(n):
        for col in range(n):
            # if self.lista[self.pick][col] == row:
            if x[col] == row:
                print ("H", end=" ")
            else:
                print ("0", end =" ")
        print()




dodaj_hetmana(0)
print(len(lista))

