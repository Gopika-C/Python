class Rectangle:
	def __init__(self, a, b):
		self.length = a
		self.breadth = b
	def area(self):
		return self.length * self.breadth
	def __lt__(self, o):
    		if self.area() < o.area():
        		return True
    		else:
        		return False

h1 = int(input("Enter length of first rectangle : "))
b1 = int(input("Enter breadth of first rectangle : "))
h2 = int(input("Enter length of second rectangle : "))
b2 = int(input("Enter breadth of second rectangle : "))
rect1 = Rectangle(h1, b1)
rect2 = Rectangle(h2, b2)
if rect1 < rect2:
	print("Rectangle 2 is greater than Rectangle 1")
else:
	print("Rectangle 1 is greater than Rectangle 2")
