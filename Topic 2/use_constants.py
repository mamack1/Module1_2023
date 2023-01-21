"""
Program: use_constants.py
Author: Michael Mack
Last date modified: 01-17-2023

The purpose of this program is to print a line using different variables from a constants file.
"""

#importing declared constants from constants.py file
import constants

#print line using all three variables
print(str(constants.QUANTITY) + " " + (constants.ITEM) + " size " + str(constants.SIZE) + ".")

#add a price constant

PRICE = 259.99

#use price with ITEM constant

print(str(constants.ITEM) + " " + "are $" + str(PRICE) + ".")

