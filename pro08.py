# pro08.py
import math
bala,vg=map(int,input().split())
sup=[]
tsp=list(map(int,input().split()))
for i in range(0,vg):
    but,hlg=map(int,input().split())
    sup.append([but,hlg])
for i in sup:
    gg=i[0]-1
    ate=i[1]-1
    print(math.gcd(tsp[gg],tsp[ate]))

    
