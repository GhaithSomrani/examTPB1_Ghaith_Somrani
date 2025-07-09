import math
Data = [1,3,5]
Prod=math.prod(Data)
print("le produit est: ",Prod)
def produit (T):
    s=0 
    for t in T:
        s*=t
        return s