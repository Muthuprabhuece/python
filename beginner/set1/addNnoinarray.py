n=int(input())
k=int(input())
a=[]
b=0
for i in range(n):
	f=int(input())
	a.append(f)
for i in range(k):
	b=b+a[i]
print(b)
