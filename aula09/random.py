import random as r

matrice1 = []
matrice2 = []

for sublist in range(10):
    sublist1 = []
    for element in range(10):
        sublist1.append(r.randint(1, 999))
    matrice1.append(sublist1)

for n in matrice1:
    print(n)

    
