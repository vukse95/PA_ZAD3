#reference:
# 1. Andrej Kaprocki
# 2. https://courses.csail.mit.edu/6.006/fall11/rec/rec20.pdf

import sys
import random

sys.setrecursionlimit(10000)

izracunato = [-3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3,
            -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3,
            -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3,
            -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3]
#racuna koliko najvise para moze da se osvoji od i-te karte do kraja
def racunaj(i):
    #nije vec obradjen slucaj
    if(izracunato[i] == -3):
        #stavlja se 0 u slucaju da nijedan od narednih slucajeva ne donosi zaradu, sto znaci da igrac u tom trenutku odustaje
        slucajevi = [0]

        #h predstavlja do koje karte se izvlaci, 4 je minimalno po pravilima igre
        for h in range(4+i,52):
            temp=proveri_pobedu(i,h)
            #provera da li nije doslo do greske. ako jeste, taj slucaj se ne moze uzeti u obzir
            if(temp!=-2):
                slucajevi.append(temp+racunaj(h))
        izracunato[i]=max(slucajevi)
    return izracunato[i]

def proveri_pobedu(i,h):
    igrac=0
    delilac=0
    #redom se deli i igracu i deliocu isti broj karata
    while(i<(h-(h-i)%2)):
        if(deck[i]==1 and igrac<=10):
                igrac+=11
        else:
            igrac+=deck[i]
        if(deck[i+1]==1 and delilac<=10):
                delilac+=11
        else:
            delilac+=deck[i+1]
        i+=2

    #ako je broj karata koji se izvlaci neparan, poslednju kartu igrac ce izvuci samo ako zbog nje nece izgubiti, sto zna u napred jer mu je raspored karata poznat
    if((h-i)%2!=0):
        if(deck[h]==1 and igrac<=10):
            igrac+=11
        else:
            if(igrac+deck[h]<=21):
                igrac+=deck[h]
            else:
                if(deck[h]==1 and delilac<=10):
                    delilac+=11
                else:
                    #ako delilac ima bolji rezultat od igraca, nema razloga da izvlaci kartu cime dolazi do greske jer kartu niko nije izvukao
                    if(delilac>igrac):
                        return -2
                    else:
                        delilac+=deck[h]
    #provera da li je podeljeno dovoljno karata
    if(igrac<17 or delilac<17):
        return -2
    #provera da li je podeljeno previse karata
    if(igrac>21 and delilac>21):
        return -2
    if(igrac>21):
        return -1
    if(delilac>21):
        return 1
    if(igrac>delilac):
        return 1
    if(igrac==delilac):
        return 0
    if(igrac<delilac):
        return -1

deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10];

for i in range (0,10):
    random.shuffle(deck)
    print("Spil: ")
    print(deck)
    print("Najvise para koliko igrac moze da osvoji: ")
    print(racunaj(0))
    for i in range(0,52):
        izracunato[i]=-3







