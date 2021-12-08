fo= open('abx.txt',"r+")
print("Name of file: ",fo.name)
hi="Hellopython is fun for everyone"
fo.write(hi)
str=fo.read(18)
print("The read string\n",str)
fo.close()