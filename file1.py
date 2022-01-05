fo = open('abc.txt', "r+")
print("Name of the file: ", fo.name)
hi = "Hellopython is fun for everyone"
fo.write(hi)
str = fo.read(18)
print("The read string is\n", str)
fo.close()