"""
Problem 1
Ask the user to enter a number.
The number is considered "frue" if it is
divisible by 6, but not divisible by 8.
State whether the number is "frue" 
(2 marks)

Inputs:
a number

Outputs:
xx is frue
xx is not frue

example:
Enter a number: 48
48 is not frue
"""

#! python3

x=input('Input a number: ')

x=float(x)
a=x%6
b=x%8

if a==0 and b!=0:
    print(str(x)+' is frue')
else:
    print(str(x)+' is not frue')