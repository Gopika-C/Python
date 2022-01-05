stud={}
n=int(input("Enter the number of students:"))
for i in range(n):
	a=input("Enter name : ")
	stud[a]=int(input("Enter the mark : "))
mark=[]
print(stud)
mark+=stud.values()
mark.sort()
a=[]
for i in mark:
	for k,v in stud.items():
		if(i==v):
			a.append(str(k))
print(a)
for i in range(n):
	print("%s %d"%(a[i],stud[a[i]]))
