a,b=raw_input().split()
for i in range(int(a)+1,int(b)):
	count=1
	for s in range(2,i+1):
		for j in range(2,i+1):
			if s*j==i:
				count+=1
	if count==1:
		print i
