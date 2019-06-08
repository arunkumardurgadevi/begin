from itertools import combinations
y2,v=map(int,input().split())
w=len(str(y2))
x=list(combinations(str(y2),w-v))
x=(sorted(x))
y="".join(x[0])
print(y)
