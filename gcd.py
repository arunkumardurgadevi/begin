import math
import functools
n1,k=map(int,input().split())
p=[int(i) for i in input().split()]
for i in range(k):
    c,d=map(int,input().split())
    t=functools.reduce(math.gcd,p[c-1:d])
    print(t)
