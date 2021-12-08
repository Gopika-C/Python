s1=input("Enter first string : ")
s2=input("Enter second string : ")
a=s1.replace(s1[0:1],s2[0:1])
b=s2.replace(s2[0:1],s1[0:1])
c=a+' '+b
print("After swapping : ",c)