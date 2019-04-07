#NxN karakteri matrise atama
import random as rand
def fonk(dizi):
    matris = []
    for i in range(len(dizi)):
        matris.append([])
        for j in range(len(dizi)):
            matris[i].append(rand.choice(dizi))#list(rand.choice(dizi))

    return matris

def matris_yazdir(matris):
    for i in range(len(matris)):
        for j in range(len(matris)):
            print(matris[i][j],end = " ")
        print()
            

dizi = ['a','b','c']
matris = fonk(dizi)
matris_yazdir(matris)
kelime = "ab"

#bozalp









