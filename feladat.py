f = open('vasarlas.csv', 'r')
nullaKoltes=0

def szamok():

    for szam in f:
        szam = szam.strip()
        tmp = szam.split(";")

def napok(tmp):
    napokSzama=0
    for nap in tmp:
        napokSzama += 1

        print(nap)


f.close()
print("Ennyi nap volt a hónapba: ")