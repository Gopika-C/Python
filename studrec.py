n=int(input("Enter number of students : "))
studlist=[]
for i in range(0,n):
	stud={}
	stud["RollNo"]=int(input("Enter roll no : "))
	stud["Name"]=input("Enter name : ")
	stud["Branch"]=input("Enter branch : ")
	studlist.append(stud)
print("RollNo Name Branch")
print()
print()
for i in range(0,n):
	print(studlist[i])