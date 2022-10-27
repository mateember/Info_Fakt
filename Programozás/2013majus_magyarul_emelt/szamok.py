import random

beolvas = open("felszam.txt", "r")
kerdesek = []
adatok = []
for adatsor in beolvas:
    adatok.append(adatsor.strip())
    if len(adatok) == 2:
        tördel = adatok[1].split()
        kerdesek.append([adatok[0], int(tördel[0]), int(tördel[1]), tördel[2]])
        adatok = []
beolvas.close()
print("2. feladat:\n" + str(len(kerdesek)), " feladat volt az adatfájlban")

print("\n3. feladat:")
mat1 = 0
mat2 = 0
mat3 = 0
for adatsor in kerdesek:
    if adatsor[3] == "matematika":
        if adatsor[2] == 1:
            mat1 += 1
        elif adatsor[2] == 2:
            mat2 += 1
        elif adatsor[2] == 3:
            mat3 += 1
print("Az adatfájlban", (mat1 + mat3 + mat2), "feladat van, 1 pontot ér", mat1, "feladat, 2 pontot ér", mat2,
      "feladat, 3 pontot ér", mat3, "feladat.")
print("\n4. feladat:")

valaszok = []
for adatsor in kerdesek:
    valaszok.append(adatsor[1])
print("A válaszok számértéke ", min(valaszok), "-től, ", max(valaszok), "-ig terjed.", sep="")

'''min1 = kerdesek[0][1]
max1 = kerdesek[0][1]
for adatsor in kerdesek:
    if adatsor[1] > max1:
        max1 = adatsor[1]
    if adatsor[1] < min1:
        min1 = adatsor[1]
'''
print("\n5.feladat:")
'''
temakorok = set()
for adatsor in kerdesek:
    temakorok.add(adatsor[3])
tlista = []
for adatsor in temakorok:
    tlista.append(adatsor)
print("Kérdések témakörei: ")
for i in range(len(tlista)-1):
    print(tlista[i] + ", ", end="")
print(tlista[-1])
'''
témakör1 = []
for adatsor in kerdesek:
    if adatsor[3] not in témakör1:
        témakör1.append(adatsor[3])
print("Kérdések témakörei: ", end="")
for i in range(len(témakör1) - 1):
    print(témakör1[i] + ", ", end="")
print(témakör1[-1])

tnev = input("Témakör név: ")
tnevlist = []
for adatsor in kerdesek:
    if tnev == adatsor[3]:
        tnevlist.append(adatsor[0])
veletlen = random.randint(0, len(tnevlist) - 1)
for adatsor in kerdesek:
    if tnevlist[veletlen] in adatsor[0]:
        kerdes = adatsor[0]
        valasz = adatsor[1]
        pont = adatsor[2]
print(kerdes)
be_valasz = input("Válasz: ")
if int(be_valasz) == valasz:
    print("A válasz ", pont, "pontot ér", sep="")
else:
    print("A válasz 0 pontot ér")
    print("Helyes válasz:", valasz)

kerdes_szamok = set()

while len(kerdes_szamok) < 10:
    kerdes_szamok.add(random.randint(0, len(kerdesek) - 1))
print(kerdes_szamok)

