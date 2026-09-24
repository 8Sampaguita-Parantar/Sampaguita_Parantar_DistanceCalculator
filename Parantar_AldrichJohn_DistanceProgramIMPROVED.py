#Author - Aldrich John P. Parantar
#Date - 8/18/2026
#Purpose - To calculate the distance between two points in a graph using built-in math functions from a library.

#STEP 1 - IMPORTING LIBRARY - Imports the math library to allow predefined math functions to exist, cutting time to make it simpler and faster.
import math

#STEP 2 - INPUT - Asks the user to input the points required to calculate the distance between 2 points: 1st point x and y, 2nd point x and y.
x1 = float(input("Enter 1st point x: "))
y1 = float(input("Enter 1st point y: "))
x2 = float(input("Enter 2nd point x: "))
y2 = float(input("Enter 2nd point y: "))

#STEP 3 - INPUT PROCESSING - Processes and calculates the distance between two points, using predefined math library functions. sqrt gets the square root of the difference of 2 points x or y, and uses pow to square it.
distance = math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))

#STEP 4 - OUTPUT DISPLAY - Displays the output from the given parameters up to two decimal places. For example:
#Enter 1st point x: 5
#Enter 1st point y: 8
#Enter 2nd point x: 1
#Enter 2nd point y: 0
#The distance between the two points is: 8.94
print(f"The distance between the two points is: {distance:.2f}")

#REFLECTION
#For me, using a math library is more practical than writing all the calculations from scratch because it is simple, direct, and easy to understand.
#For instance, math.sqrt and math.pow in my program made it very simple, fast, and readable, only needing quick functions instead of manually typing a complex equation or algorithm.
#In conclusion, the library helped me make the program more efficiently and faster, preventing errors from slipping in.