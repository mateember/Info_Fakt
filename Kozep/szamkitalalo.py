import random
szam = random.randint(1, 100)
tipp = int(input("Tippelj egy számra: "))


for i in range(2,4):

    while tipp != szam:
        tipp = int(input("Tippelj újra: "))
        i = i + 1
        print(i)
        if i  >= 3:
            break
if tipp == szam:
    print("Nyertél")
