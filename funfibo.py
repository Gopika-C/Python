def fib(n):
	if(n<=1):
		return(n)
	elif(n>0):
		return(fib(n-1)+fib(n-2))
num=int(input("Enter limit : "))
for i in range(0,num):
	r=fib(i)
	print(r)
