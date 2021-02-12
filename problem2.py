#! python3

"""
Problem 2
Factors are positive integers that divide evenly into another integer.
The user will enter in two numbers. Determine if the smaller is a factor of the larger
(2 marks)

inputs:
an integer
an integer

outputs:
xx is a factor of yy
xx is not a factor of yy

examples:
Enter a number: 10
Enter another number: 2
2 is a factor of 10

Enter a number: 4
Enter another number: 25
4 is not a factor of 25
"""

x=int(input('Enter an integer: '))
y=int(input('Enter another integer: '))

if (x>y)==True:
    num1=x
    num2=y
else:
    num1=y
    num2=x
value=num1%num2
if value==0:
    print(str(num2)+' is a factor of '+str(num1))
else:
    print(str(num2)+' is not a factor of '+str(num1))