n=int(input("Enter the number of students : "))
studlist=[]
for i in range(0,n):
	stud={}
	stud["RollNo"]=int(input("Enter roll number : "))
	stud["Name"]=input("Enter the name : ")
	stud["Attendence"]=int(input("Enter the attendence : "))
	studlist.append(stud)
for i in range(1,n):
	for j in range(0,n-1):
		if(studlist[j]["Attendence"]<studlist[j+1]["Attendence"]):
			temp=studlist[j]
			studlist[j]=studlist[j+1]
			studlist[j+1]=temp
print("Attendence list")
for i in range(0,n):
	print(studlist[i])
