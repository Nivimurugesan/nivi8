Kk1=int(input())
nn1=list(map(int,input().split()))
li=[]
for y in range(Kk1):
    for i in range(y+1,len(nn1)):
        if(nn1[i]==nn1[y]):
          li.append(nn1[y])
if (len(li)==0):
    print("unique")
else:
    li.sort()
    li2=set(li)
    for y in li2:
        print(y,end=" ")
