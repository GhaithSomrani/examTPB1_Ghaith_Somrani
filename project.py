import math
Data = [1,3,5]
Prod=math.prod(Data)
print("le produit est: ",Prod)
def produit (T):
    s=0 
    for t in T:
        s*=t
        return s
if Data:
    print("le produit est: ",produit(Data))
    print("le produit est: ",min(Data))
    print("le produit est: ",max(Data))
else:
    print('dossier vide')