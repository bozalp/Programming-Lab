def sifirlar(matris):
    count = 0
    for i in range(len(matris)):
        for j in range(len(matris)):
            if(matris[i][j] == 0):
                count += 1
    oran = (count * 100) / (len(matris) * len(matris)) 
    
    return oran

def matrisden_hashe(matris):
    hash_table = {}
    oran = sifirlar(matris)
	
    print(end = "\n")
    for i in range(len(matris)):
        for j in range(len(matris)):
            if(oran < 30.0):
                hash_table[(i,j)] = matris[i][j]
    return hash_table


    #print_hash
def print_hash_table(hash_table):
    for i in hash_table:
        print(hash_table[i],end = ",")
    
    
matris = [[12,1],[1,0]]
print("sifir orani : %",sifirlar(matris))
print_hash_table(matrisden_hashe(matris))

#bozalp