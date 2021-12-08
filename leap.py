start=int(input("Enter the starting year : "))
last=int(input("Enter the last year : "))
print("list of leap year\n")
for year in range(start,last+1):
	if(year%4==0 and year%100!=0 or year%400==0):
		print(year)

	
