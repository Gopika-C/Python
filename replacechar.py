str=input("Enter the string : ")
s=str[0]
for i in range(len(str)):
	str=str.replace(str[0],'$')
	str1=s+str[1:]
print(str1)