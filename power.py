def pow(x,n):
	if n==0:
		return(1)
	else:
		return(x*pow(x,n-1))
a=int(input("Enter the number : "))
b=int(input("Enter the power : "))
r=pow(a,b)
print("Power of the number is ",r)