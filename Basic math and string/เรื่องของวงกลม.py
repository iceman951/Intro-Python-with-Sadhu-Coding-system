import math
print("******************************\n*********About Circle*********\n******************************")
radius = float(input("Input radius: "))
print("Radius is",radius)
Circumference = 2*math.pi*radius
print("Circumference is {:.4f}".format(Circumference))
Area = math.pi*radius*radius
print("Area is {:.2f}".format(Area))
y = float(input("Enter y for finding x: "))
x = math.sqrt((radius**2)-(y**2))
print("y is {:.4f}".format(y))
print("x is {:.4f} and {:.4f}".format(x*(-1),x))
print("******************************")