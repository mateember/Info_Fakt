print('1. feladat')
beolvas = open('szavazatok.txt', "r")
szavazatok = []
for sor in beolvas:
    szavazat = sor.strip().split(' ')
    szavazatok.append([int(szavazat[0]), int(szavazat[1]), szavazat[2], szavazat[3], szavazat[4]])

#print(szavazatok)

print('2.feladat:\nA helyhatósági választáson', int(len(szavazatok), ), 'képviselőjelölt indult.')

print('3. feladat: ')
be_vnev = input('Adja meg a képviselő vezetéknevét: ')
be_unev = input('Adja meg a képviselő keresztnevét: ')
be_nev = be_vnev + ' ' + be_unev
#print(be_nev)

for teszt in szavazatok:
    if str(teszt[2]) + " " + str(teszt[3]) == be_nev:
        print('A jelölt', teszt[1], 'szavazatot kapott')
    else:
        print('Ilyen nevű képviselőjelölt nem szerepel a nyilvántartásban!')
        break