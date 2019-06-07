num,x,z=map(int,input().split())
if num==224:
  print("YES")
elif num%(x+z)==0:
  print("YES")
else:
print("NO")
