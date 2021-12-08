def exchange(str):
	return str[-1:]+str[1:-1]+str[:1]
str=input("Enter the string : ")
print("String after exchange : ")
print(exchange(str))