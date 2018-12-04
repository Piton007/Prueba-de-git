import time
def Monto_Sencillar_DP(monto,coins):
    C_M=[0]*(monto+1)
    Coins_used=[0]*(monto+1)
    for i in range(monto+1):
        Coins_used[i]=[0]*len(coins)
    def Recursivo(Estado_Actual):
        if Estado_Actual==0:
            return
        else:
            Recursivo(Estado_Actual-1)
            aux=[]
            aux2=[]
            for i in range(len(coins)):
                if Estado_Actual>=coins[i]:
                    aux.append(C_M[Estado_Actual-coins[i]])
                    aux2.append(coins[i])
            a=min(aux)
            C_M[Estado_Actual]=a+1
            aux1=Estado_Actual-aux2[aux.index(a)]
            for i in range(len(coins)):
                if coins.index(aux2[aux.index(a)])!=i:
                    Coins_used[Estado_Actual][i]=Coins_used[aux1][i]
                else:
                    Coins_used[Estado_Actual][i]=Coins_used[aux1][i]+1
    
    Recursivo(monto)
    print(C_M)
    for i in range(len(coins)):
        enunciado=""
        enunciado+=str(Coins_used[monto][i])+str(" monedas de: ")+str(coins[i])+str("\t")
        print(enunciado)
a=time.perf_counter()
Monto_Sencillar_DP(190,[1, 5, 10, 20, 25, 50])
b=time.perf_counter()
print('{0:.2f}'.format(b-a))
