from itertools import combinatiions
num,n=map(int,input().split())
x=len(str(num))
l=list(combinations(str(num),x-num))
l=sorted(l))
y="".join(l[0])
print(y)
