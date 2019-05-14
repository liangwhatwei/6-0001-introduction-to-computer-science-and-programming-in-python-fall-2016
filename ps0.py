import math #import maths module for log function
x = int (input("Enter number x: ")) # ask user to input x
y = int (input("Enter number y: ")) # ask user to input y
power = x**y #x power of y
print("x**y is",power) #print power
log = math.log (x,2) #log x with base of 2
log = int(log) #convert float type to int type for log
print ("log(x) = ",log) #print log(x)