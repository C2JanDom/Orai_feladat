f = open('vasarlas.csv', 'r')
napokSzama=0

for szam in f:
    szam = szam.strip()
    tmp = szam.split(";")

    print(tmp)

f.close()