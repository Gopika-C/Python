def conv(n):
	s=0
	i=0
	while(n>0):
		r=n%10
		s=s+r*(2**i)
		i=i+1
		n=n//10
	print(s)
f=int(input("Enter a binary value\n"))
print("Decimal value of",f)
conv(f)
