#Author - Aldrich John P. Parantar
#Date - 8/18/2026
#Purpose - To calculate the distance between two points in a graph using built-in math functions from a library.

import math

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))

print(f"The distance between the two points is: {distance:.2f}")

#REFLECTION
#For me, using a math library is more practical than writing all the calculations from scratch because it is simple, direct, and easy to understand.
#For instance, math.sqrt and math.pow in my program made it very simple, fast, and readable, only needing quick functions instead of manually typing a complex equation or algorithm.
#In conclusion, the library helped me make the program more efficiently and faster, preventing errors from slipping in.