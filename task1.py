#! python3
# Ask the user for their name and their email address.
# (2 points)
#
# Inputs:
# name
# email
#
# Sample output:
# Your name is Joe Lunchbox, and your email is joe@koolsandwiches.org.

name=input("Enter your name")
email=input("Enter your email")
print("Your name is ",end="")
print(name,end="")
print(", and your email is ",end="")
print(email,end="")
print(".",end="")
