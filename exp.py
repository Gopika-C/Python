x=int(input("Enter x : "))
n=int(input("Enter n : "))
s=1
def fac(n):
	f=1
	for i in range(1,n+1):
		f=f*i
	return(f)
for i in range(1,n):
	s=s+(x**i)/fac(i)
print(s)