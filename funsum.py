def sum(n):
	s=0
	for i in range(1,n+1):
		s=s+i
	return s
n=int(input("Enter a limit : "))
print("Sum till",n,"is",sum(n))

		