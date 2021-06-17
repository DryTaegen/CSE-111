import math
#What are in and not in?
#in
#not in 

x = 5
y = 6

print(y == x)
#output = false


name = "Joey"

print("J" in name)
#output = true

print("j" in name)
#output = false

print("a" not in name)
#output = true

# value X= value2. Value will be changed by value2 by using the mechanic of X. X can = *,-,+,/,%, etc
#anything within a function is a parameter or an argument: function(parameter, parameter)
def computeCircumfrence(radius):
    return math.pi * radius * 2

print(computeCircumfrence(float(input("What is the radius? "))))