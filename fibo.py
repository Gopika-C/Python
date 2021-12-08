def fibo(num):
	a=0
	b=1
	for i in range(2,num):
		c=a+b
		print(c)
		a=b
		b=c
		
num=int(input("Enter the number:"))
if(num==1):
	print(0)
elif(num==2):
	print(0,1)
else:
	print(0)
	print(1)
	fibo(num)









