s,t=raw_input().split()
for v in range(int(s),int(t)+1):
	b=v
	a=b
	c=1
	e=0
	while a>10:
		a=a/10
		c=c+1
	while b>0:
		d=b%10
		b=b/10
		e=e+d**c
		d=0
	if v==e:
		print v
