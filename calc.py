def add(x,y):
	return x+y
def sub(x,y):
	return x-y
def mul(x,y):
	return x*y
def div(x,y):
	return x/y
def pow(x,y):
	return x**y
def mod(x,y):
	return x%y

print("Select Operations\n1-Add\n2-Subtract\n3-Multiply\n4-Division\n5-Power\n6-Modulus")
choice=input("Enter choice(1/2/3/4/5/6) : ")
num1=int(input("Enter first number : "))
num2=int(input("Enter second number : "))
if choice=='1':
	print(num1,"+",num2,"=",add(num1,num2))
elif choice=='2':
	print(num1,"-",num2,"=",sub(num1,num2))
elif choice=='3':
	print(num1,"*",num2,"=",mul(num1,num2))
elif choice=='4':
	print(num1,"/",num2,"=",div(num1,num2))
elif choice=='5':
	print(num1,"^",num2,"=",pow(num1,num2))
elif choice=='6':
	print(num1,"%",num2,"=",mod(num1,num2))
else:
	print("Invalid input")
