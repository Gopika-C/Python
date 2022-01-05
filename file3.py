fn = open('test.txt', 'r')

fn1 = open('newfile1.txt','w+')

cont = fn.readlines()

print(cont)

print(len(cont))

for i in range(0, len(cont)):

   if (i % 2 == 0):

	    fn1.write(cont[i])

   else:

	   	continue

fn1.close()

fn1 = open('newfile.txt', 'r')

print(fn1.read())

fn1.close()

