a=input()
count=1
for i in range(2,a+1):
	for j in range(2,a+1):
		if i*j==a:
			count+=1
print count
if count==1:
	print "yes"
else:
	print "no"
