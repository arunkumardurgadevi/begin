x3=input()
x3=int(x3)
a1=[]
for j in range(0,x3):
    n1=input()
    a1.append(n1)
f1=[]
for j in zip(*a1):
    if j.count(j[0])==len(j):
        f1.append(j[0])
    else:
        break
print(''.join(f1))
