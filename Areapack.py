from Graphics.RectFunctions import*
from Graphics.CirFunctions import *
from Graphics.DGraphics.SphereFunctions import *
from Graphics.DGraphics.CuboidFunctions import *
l=int(input("Enter the length of Rectangle : "))
b=int(input("Enter the breadth of Rectangle : "))
print("Area = ",RectArea(l,b))
print("Perimeter = ", RectPerimeter(l,b))

r=int(input("Enter the radius of a circle : "))
print("Circle area = ",CirArea(r))
print("Circle Perimeter = ", CirPerimeter(r))

r=int(input("Enter the radius of Sphere:"))
print("Sphere area = ",SpArea(r))
print("Sphere Perimeter = ", SpPerimeter(r))

l=int(input("Enter the  length of Cuboid : "))
b=int(input("Enter the breadth of Cuboid : "))
h=int(input("Enter the height of Cuboid : "))
print("Cuboid area = ",CuboidArea(l,b,h))
print("Cuboid Perimeter =",CuboidPerimeter(l,b,h))
