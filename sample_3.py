#tersten okunus
def tersten_oku(kelime):
    d3 = []
    for i in range(len(kelime)-1,-1,-1):
        d3.append(kelime[i])
    #print(d3)
    print(list(kelime))
    if list(kelime) == list(d3):
        print("aynı bea")
    else:
        print("aynı degil")
    print(d3)

kelime = "COMU" 
print(list(kelime))

tersten_oku(kelime)
print(kelime)
print(kelime[::-1])

dizi = "CANAKKALE"
for i in range(len(dizi)):
    print(dizi[i])
    
#bozalp