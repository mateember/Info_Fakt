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
for sor2 in szavazatok:
    szavazott = szavazott + int(sor2[1])

arany = (szavazott / jogosult) * 100
print("A választáson", str(szavazott), "állampolgár, a jogosultak", "%.2f" % arany + "%-a vett részt.\n")

print("5. feladat:")

gyep = 0.0
hep = 0.0
tisz = 0.0
zep = 0.0
fuggetlen = 0.0

for i in szavazatok:
    if i[4] == '-':
        fuggetlen = fuggetlen + float(i[1])
    elif i[4] == 'GYEP':
        gyep = gyep + float(i[1])
    elif i[4] == 'HEP':
        hep = hep + float(i[1])
    elif i[4] == 'TISZ':
        tisz = tisz + float(i[1])
    elif i[4] == 'ZEP':
        zep = zep + float(i[1])

osszszavazat = 0

for i in szavazatok:
    osszszavazat = osszszavazat + i[1]
print("Gyümülcsevők Pártja: " + "%.2f" % ((gyep / osszszavazat) * 100) + "%")
print("Húsevők Pártja: " + "%.2f" % ((hep / osszszavazat) * 100) + "%")
print("Zöldségevők Pártja: " + "%.2f" % ((zep / osszszavazat) * 100) + "%")
print("Tejivók Szövetsége: " + "%.2f" % ((tisz / osszszavazat) * 100) + "%")
print("Független jelöltek: " + "%.2f" % ((fuggetlen / osszszavazat) * 100) + "%")

print("\n6. feladat")

legtobb = 0
legtobbsz = [0]
for j in szavazatok:
    if legtobb < j[1]:
        legtobb = j[1]
        legtobbsz[0] = j[1]

for i in szavazatok:
    if legtobbsz[0] == i[1]:
        print("A legtöbb szavazatot", i[2], i[3], "kapta, ", end="")
        if i[4] == "-":
            print("független képviselő.")
        else:
            print("a", i[4], "párt jelöltje")
