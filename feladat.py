f = open('vasarlas.csv', 'r')
nullaKoltes=0


for szam in f:
    szam = szam.strip()
    tmp = szam.split(";")

def napok(tmp):
    napokSzama=0
    for nap in tmp:
        napokSzama += 1
    print("Ennyi nap volt a hónapba: ", napokSzama)


f.close()
napok(tmp)