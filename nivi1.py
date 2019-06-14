import math
import functools
a,b=map(int,input().split())
List=[int(i) for i in input().split()]
for i in range(b):
    cc,dd=map(int,input().split())
    t=functools.reduce(math.gcd,List[cc-1:dd])
    print(t)
