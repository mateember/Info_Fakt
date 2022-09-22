print('1. feladat\n')
beolvas = open('szavazatok.txt', "r")
szavazatok = []
for sor in beolvas:
    szavazat = sor.strip().split(' ')
    szavazatok.append([int(szavazat[0]), int(szavazat[1]), szavazat[2], szavazat[3], szavazat[4]])

# print(szavazatok)

print('2.feladat:\nA helyhatósági választáson', int(len(szavazatok), ), 'képviselőjelölt indult.\n')

print('3. feladat: ')
be_vnev = input('Adja meg a képviselő vezetéknevét: ')
be_unev = input('Adja meg a képviselő keresztnevét: ')
be_nev = be_vnev + ' ' + be_unev
# print(be_nev)
Letezik = False
for sor1 in szavazatok:
    tnev = str(sor1[2]) + " " + str(sor1[3])
    if tnev == be_nev:
        print('A jelölt', sor1[1], 'szavazatot kapott\n')
        Letezik = True

if not Letezik:
    print('Ilyen nevű képviselőjelölt nem szerepel a nyilvántartásban!\n')

print("4.feladat")
jogosult = 12345
szavazott = 0
for sor in szavazatok:
    szavazott += int(sor[1])

arany = (szavazott / jogosult) * 100
print("A választáson", str(szavazott), "állampolgár, a jogosultak", "%.2f" % arany + "%-a vett részt.\n")

print("5. feladat:")

szervezetek = [["Gyümülcsevők Pártja", "GYEP"],
               ["Húsevők Pártja", "HEP"],
               ["Zöldségevők Pártja", "ZEP"],
               ["Tejivók Szövetsége", "TISZ"],
               ["Független jelöltek", "-"]
               ]

for szervezet in szervezetek:
    voksok = 0
    for sor in szavazatok:
        if szervezet[1] == sor[4]:
            voksok += sor[1]
    print(szervezet[0] + ": " + str(round((voksok / szavazott) * 100, 2)) + "%")

'''gyep = 0.0
hep = 0.0
tisz = 0.0
zep = 0.0
fuggetlen = 0.0

for i in szavazatok:
    if i[4] == '-':
        fuggetlen += float(i[1])
    elif i[4] == 'GYEP':
        gyep += float(i[1])
    elif i[4] == 'HEP':
        hep += float(i[1])
    elif i[4] == 'TISZ':
        tisz += float(i[1])
    elif i[4] == 'ZEP':
        zep += float(i[1])


print("Gyümülcsevők Pártja: " + "%.2f" % ((gyep / szavazott) * 100) + "%")
print("Húsevők Pártja: " + "%.2f" % ((hep / szavazott) * 100) + "%")
print("Zöldségevők Pártja: " + "%.2f" % ((zep / szavazott) * 100) + "%")
print("Tejivók Szövetsége: " + "%.2f" % ((tisz / szavazott) * 100) + "%")
print("Független jelöltek: " + "%.2f" % ((fuggetlen / szavazott) * 100) + "%")
'''
print("\n6. feladat")

legtobb = 0
legtobbsz = 0
for sor in szavazatok:
    if legtobb < sor[1]:
        legtobb = sor[1]
        legtobbsz = sor[1]

print("A legtöbb szavazatot kapó képviselőjelöltek, (", legtobbsz, ") szavazattal:", sep="")

for sor in szavazatok:
    if legtobbsz == sor[1]:
        print(sor[2], sor[3], end="")
        if sor[4] == "-":
            print(", független képviselő.")
        else:
            print(", a", sor[4], "párt jelöltje.")
'''
for sor in szavazatok:
    if legtobbsz == sor[1]:
        print("A legtöbb szavazatot", sor[2], sor[3], "kapta, ", end="")
        if sor[4] == "-":
            print("független képviselő", end="")
        else:
            print("a", sor[4], "párt jelöltje", end="")
        print(", (", legtobbsz, ") szavazattal.", sep="")'''

print("7.feladat")
# rendezzük az adatokat választókerület és szavazato száma szerint szerint
for i in range(len(szavazatok)):
    for j in range(len(szavazatok)-i-1):
        if szavazatok[j][0] > szavazatok[j+1][0]:
            csere = szavazatok[j]
            szavazatok[j] = szavazatok[j+1]
            szavazatok[j+1] = csere

for i in range(len(szavazatok)):
    for j in range(len(szavazatok)-i-1):
        if szavazatok[j][0] >= szavazatok[j+1][0] and szavazatok[j][1] < szavazatok[j+1][1]:
            csere = szavazatok[j]
            szavazatok[j] = szavazatok[j+1]
            szavazatok[j+1] = csere
for sor in szavazatok:
    print(sor)
beolvas.close()
