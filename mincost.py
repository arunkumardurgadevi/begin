m5,n5=input().split()
ob=abs(len(m5)-len(n5))
for i in range(len(m5)):
	if len(n5)==1 and n5[i] in m5:
		break
	elif i>=len(m5) or i>=len(n5):
		break
	elif n5[i]!=n5[i] and n5[i]:
		ob=ob+1
print(ob)
