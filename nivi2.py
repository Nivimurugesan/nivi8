
aa=int(input())
ss=list(map(int,input().split()))
yy=sorted(ss)[::-1]
zz=""
if(ss==[0]*aa):
    print("0")
else:
    for j in yy:
        zz=zz+str(j)
    print(int(zz))
