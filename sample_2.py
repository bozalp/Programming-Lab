#standart sapma
import math


def fonk(x):
    top = 0
    N = len(x)
    x_ort = sum(x) / N
    
    for i in range(N):
        top += ((x[i] - x_ort)**2)
    
    sonuc = top/(N-1)
    return math.sqrt(sonuc)

x = [17, 77, 97, 5, 6, 7]
print(fonk(x))

#bozalp