def asal_carpanlarina_ayirma(sayi):
    liste=[]
    asal_liste=[1,sayi]
    asal=False
    for i in range(2,sayi):#2den sayiya kadar  
        if(int(sayi)%i==0):
            liste.append(i)
            asal=True
    else:
        if(asal == True):
            print("Asal Degil")
            return liste
        else:
            print("Asal")
            return asal_liste
    
print(asal_carpanlarina_ayirma(42))
        

print("\n----------------------\n")

dizi=[1,1,1,1]
def en_buyuk_toplam_bul(arr):
    sonuc=[]
    toplam=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            for k in range(i,j+1):
                toplam+=arr[k]
            sonuc.append(toplam)
            toplam=0
            print(sonuc)
            
    buyuk_sayi=0
    for i in range(len(sonuc)):
        if(sonuc[i]>buyuk_sayi):
            buyuk_sayi=sonuc[i]
    return buyuk_sayi
    


print(en_buyuk_toplam_bul(dizi))



            
#bozalp