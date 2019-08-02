# pro08.py
import math
viji,lak=map(int,input().split())
sug=[]
ttt=list(map(int,input().split()))
for i in range(0,lak):
    lac,hac=map(int,input().split())
    sug.append([lac,hac])
for i in sug:
    den=i[0]-1
    eat=i[1]-1
    print(math.gcd(ttt[den],ttt[eat]))

