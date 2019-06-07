a=int(input())
b=input().split()
c=0
for i in range(len(b)):
  c+=int(b[i])
print(c//len(b))
