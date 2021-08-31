############################
# Learn Python Coding 2019 with Codemy.com
# Instructor: John Elder 
# Instructor Github: https://github.com/flatplanet
# 
# Student: PsyPhyber
############################

############################
# Data Types
# Strings
# Numbers
# Lists
# Tuples
# Dictonaries
# Boolean
#############################

#############################
#
# Clear the terminal screen with os.system 'clear'
#
#############################

import os
os.system('clear')

print ("Hello World!")

#############################
#
# Strings 
# subject name = 'returned information'
#
#############################

name = 'PsyPhyber'
age = 55

#############################
#
# Create a list by subject name = ["information"]
# Use commas between each "information", "information"
#
#############################

names = ["PsyPhyber", "Tim", "Jack", "Molly"]

#############################
#
# To write a List as Tuples use ("name") instead of ["name"]
# Tuples cannot be changed!
# Use Tuples with caution!
#
##############################

##############################
#
# Create a Dictonary using { }
#
##############################

fav_pizza = {
	"PsyPhyber": "pepperoni",
	"Tim": "pepperoni",
	"Jack": "pepperoni",
	"Molly": "cheese"
	}

###############################
#
# Boolean is a True or False tool
# Can be utilized for if True or False return functions
#
###############################

name = True
print (name)

print ("My name is " + names[0] + ".")
print ("I like " + fav_pizza["PsyPhyber"] + " pizza.")

###############################
#
# Use single quote 'text and then "double quotation inside"'
# Also can use Python escape characters \
# or can use \n\ for new line
# Example: "My Boss Yelled \"GET BACK TO WORK!\""
# or "My Boss Yelled \n\ "GET BACK TO WORK!\"" to look like
# My Boss Yelled
# "GET BACK TO WORK!"
#
###############################

greetings = 'My Boss Yelled "GET BACK TO WORK!"'
print(greetings)

###############################
#
# Concantenating
#
###############################

name = "PsyPhyber"
greetings = "Hello, my name is " + name

print(greetings.upper())

###############################
#
# Can also use (greeting.lower()), (greeting.title()), 
# (greeting.swapcase()), ect.
#
###############################

print(len(greetings))

###############################
#
# (len(greeting)) is the length
# will show number of spaces or characters
# len can be used to isolate or split sections of characters
#
###############################

print(name + " is great thanks to codemy.com!")

greetings = "Is this a flat world?"
print(greetings[10:21])

print(greetings.split(" "))

print(greetings.split(" ")[3:5])

###############################
#
# Numbers
# Integer is whole number 1, 2, 3, ect.
# Float is .25, .35, .42, ect.
#
###############################

num = 10
print(num)

###############################
#
# Change (num) to float as follows:
# Will be 10.0 instead of 10
#
###############################

num = 10
print(float(num))

num = 10.25
print(int(num))

print(7+2)
print(7-2)
print(7*2)
print(7/2)
print(5**4)

###############################
#
# ** = to the power of
#  % = modulus is the remainder
# 
###############################

print(10%2)
print(10%3)

num_1 = 5
num_2 = 2
print(num_1 * num_2)

###############################
#
# Order of Operations matter
# Remember PEMADS
#
###############################

# 15 or 7?

print("Does writing (4 + 1 * 3) in Python = 15 or 7?")
print(4 + 1 * 3)
print("Now, let us look at writing it like ((4 + 1) * 3)")
print((4 + 1) * 3)
print("The ( ) make a difference - PEMADS applies in Python")

