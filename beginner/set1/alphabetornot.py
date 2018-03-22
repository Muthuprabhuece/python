a=raw_input()
b=0
for c in range(ord('a'),ord('z')):
	if a==chr(c):
		b=1
if b==1:
	print("Alphabet")
else:
	print("No")
