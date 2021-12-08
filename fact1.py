def rec(n):
	if(n==1):
		return 1
	else:
		return n*rec(n-1)
num=int(input("Enter a number \n"))
if(num<0):
	print("Factorial doesnot exist")
elif(num==0):
	print("Factorial of num is 1 ")
else:
	print("Factorial of number : ",rec(num))
		
