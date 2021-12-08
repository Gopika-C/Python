w=input('enter the string:')
a=[]
str= w.split()
for i in str:
    if i not in a:
        a.append(i)
print(a)