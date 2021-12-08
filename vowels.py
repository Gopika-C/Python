word=input("Enter a string \n")
vowels=['a','e','i','o','u']
list=[]
for i in word:
	if(i in vowels and i not in list):
		list.append(i)
print("Vowels in list \n",list)
