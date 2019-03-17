
coinlist=[1, 5, 25, 21]
coin = (int(input("Coin : ")))
knownResults = [0 for i in range(coin + 1)]

def recMC(coinlist,change):
    mincoin = change
    if(change in coinlist):
        knownResults[change] = 1
        return 1
    elif knownResults[change] > 0:
        return knownResults[change]
    else:
        for i in [c for c in coinlist if c <= change]:
            numcoin = 1 + recMC(coinlist, change - i)
            if numcoin < mincoin:
                mincoin = numcoin
                knownResults[change] = mincoin
    return mincoin

print("Recursive Result -> ",recMC(coinlist, coin))



#bozalp