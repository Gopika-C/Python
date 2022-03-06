a =[]
n = int(input("Enter the number of words:"))
for i in range(0, n):
    m = input("Enter the word:")
    a.append(m)
max_length =len(a[0])
temp=a[0]
for i in a:
     if (len(i)>max_length):
            max_length=len(i)
            temp=i
print("Longest word is:",temp)
print("Length of longest word is:",max_length)
