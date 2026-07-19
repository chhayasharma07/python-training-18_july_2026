# 1. Area and Perimeter of Square, Circle and Triangle

import math

# Square
side=float(input("Enter the side of the square : "))

square_area=side*side
square_perimeter=4*side

print(f"Area of square is {square_area}")
print(f"Perimeter of square is {square_perimeter}")

# Circle
radius=float(input("Enter the radius of the circle : "))

circle_area=math.pi*radius*radius
circle_perimeter=2*math.pi*radius

print(f"Area of circle is {circle_area}")
print(f"Circumference of circle is {circle_perimeter}")

# Triangle
base=float(input("Enter the base of the triangle : "))
height=float(input("Enter the height of the triangle : "))
side1=float(input("Enter the first side : "))
side2=float(input("Enter the second side : "))
side3=float(input("Enter the third side : "))

triangle_area=0.5*base*height
triangle_perimeter=side1+side2+side3

print(f"Area of triangle is {triangle_area}")
print(f"Perimeter of triangle is {triangle_perimeter}")

# 2. Surface Area and Volume of Cube, Cylinder, Cone and Cuboid

import math

# Cube
side=float(input("Enter the side of the cube : "))

cube_surface_area=6*side*side
cube_volume=side*side*side

print(f"Surface area of cube is {cube_surface_area}")
print(f"Volume of cube is {cube_volume}")

# Cylinder
radius=float(input("Enter the radius of the cylinder : "))
height=float(input("Enter the height of the cylinder : "))

cylinder_surface_area=2*math.pi*radius*(radius+height)
cylinder_volume=math.pi*radius*radius*height

print(f"Surface area of cylinder is {cylinder_surface_area}")
print(f"Volume of cylinder is {cylinder_volume}")

# Cone
radius=float(input("Enter the radius of the cone : "))
height=float(input("Enter the height of the cone : "))

slant_height=math.sqrt(radius*radius+height*height)

cone_surface_area=math.pi*radius*(radius+slant_height)
cone_volume=(1/3)*math.pi*radius*radius*height

print(f"Surface area of cone is {cone_surface_area}")
print(f"Volume of cone is {cone_volume}")

# Cuboid
length=float(input("Enter the length of the cuboid : "))
breadth=float(input("Enter the breadth of the cuboid : "))
height=float(input("Enter the height of the cuboid : "))

cuboid_surface_area=2*((length*breadth)+(breadth*height)+(length*height))
cuboid_volume=length*breadth*height

print(f"Surface area of cuboid is {cuboid_surface_area}")
print(f"Volume of cuboid is {cuboid_volume}")