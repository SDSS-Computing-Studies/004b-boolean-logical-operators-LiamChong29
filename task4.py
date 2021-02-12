#! python3
"""
Ask the user to enter a name. 
If the name is one of the names on a list of special users, greet them by name.
(2 points) 

Inputs:
Name (string)

Outputs:
You are not a VIP.
Hi xxxxxx! You are a VIP!

Example:
Enter your name=>Gertrude
Hi Gertrude! You are a VIP!

Enter your name=>Gordon
You are not a VIP.
"""

VIPNames = ("Guile","Blanka","Christine","Carol","Richard","Daniel","Chun-Li")

x=input('Enter a name: ')
if 'Guile'in x or 'Blanka' in x or 'Christine' in x or 'Carol' in x or 'Richard' in x or 'Daniel' in x or 'Chun-Li' in x:
    print('Hi '+x+'! You are a VIP!')
else:
    print('You are not a VIP.')
