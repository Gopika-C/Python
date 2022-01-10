class Rectangle:
	def _init_(self):
		self.length=int(input("Enter the length : "))
		self.breadth=int(input("Enter the breadth : "))
	def area(self):
		self.a=self.length*self.breadth
		print("Area of Rectangle : ",self.a)
		return self.a
	def perimeter(self):
		self.p=2*(self.length+self.breadth)
		print("Perimeter of Rectangle : ",self.p,"\n")

x=Rectangle()
x._init_()
print("\n_Rectangle 1_ ")
a1=x.area()
x.perimeter()
y=Rectangle()
y._init_()
print("\n_Rectangle 2_")
b1=y.area()
y.perimeter()
if a1>b1:
	print("\nRectangle 1 is bigger.\n")
elif a1==b1:
	print("\nBoth rectangles are of same area.\n")
else:
	print("\nRectangle 2 is bigger.\n")