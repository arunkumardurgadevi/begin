s,t=map(str,input().split())
t1=0
if len(s)>len(t):
  s,t=t,s
i=0
while i<len(s):
  t1+=(ord(t[i])-ord(s[i]))
  i+=1
for i in range(i,len(t)):
  t1+=ord(t1[i])-ord('a')+1
print(t1)
