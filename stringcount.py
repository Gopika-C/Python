s1=input("Enter the string : ")
freq = {}
for i in s1:
    if i in freq:
        freq[i]+=1
    else:
        freq[i] = 1
print("Count of each characters in ",s1," is :\n ",str(freq))

