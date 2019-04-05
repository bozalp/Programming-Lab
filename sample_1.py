def toplam_matris(matris):
    d1 = []
    d2 = []
    for i in range(len(matris)):
        d1.append(0)
        d2.append(0)
    print(d1,d2,sep="\n")
    
    for i in range(len(matris)):
        for j in range(len(matris)):
            d1[i] += matris[i][j]
            d2[i] += matris[j][i]
    print("Satirlar toplami en buyuk sayinin indexi : ",d1.index(max(d1))+1)
    print("Satirlar toplami en kucuk sayinin indexi : ",d1.index(min(d1))+1)
    print("Satirlar max-min toplam : ",max(d1),"-",min(d1))
    
    print("Sutunlar toplami en buyuk sayinin indexi : ",d2.index(max(d2))+1)
    print("Sutunlar toplami en kucuk sayinin indexi : ",d2.index(min(d2))+1)
    print("Sutunlar max-min toplam : ",max(d2),"-",min(d2))    
    return d1,d2


matris = [[5,4,5,5],[6,4,4,4],[7,1,2,3],[6,7,27,4]]

for i in range(len(matris)):
    for j in range(len(matris)):
        print(matris[i][j],end=" ")
    print(end="\n")
    
print(end="\n")


print(toplam_matris(matris))

#bozalp