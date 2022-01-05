f=input("Enter the filename : ")
try:
	f1=open(f,"r")
except IOError:
	print("No file named",f)