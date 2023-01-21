"""
Program: cast_to_integer.py
Author: Michael Mack
Last date modified: 01-18-23

The purpose of this program is to accept any input,
convert to a integer type and output the integer.

"""

#grabbing users height in inches and assigning to a variable
user_height = input("Enter your height in inches: ")

#casting height into an integer
height_plus_11_inches = int(float(user_height)) + 11

#print their height plus 11 inches
print("11 inches added to you're height is: " + str(height_plus_11_inches))

#shorthand
user_height = int(float(input("Enter your height in inches: ")))
height_plus_11_inches = user_height + 11
print("11 inches added to you're height is: " + str(height_plus_11_inches))




#Modify these comments with your inputs you tested; it is fine if your expected output isn't your actual output
# Input         Expected Output         Actual Output
#    56               67                      67
#   342.695          353                      353
#   'abernathy'      error?                  Value Error