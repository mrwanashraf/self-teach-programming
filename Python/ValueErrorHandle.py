#!/usr/bin/python
'''
Script that accepts User Input
'''
# if the condition is True keep looping
while True:
    # Try this code if it has any error go to except condition
    try:
        # storing an input in a variable
        USER_INPUT = int(raw_input('Please input number only\nINPUT > '))
        # if user input is an integer print it
        if isinstance(USER_INPUT, int):
            print 'Your input is {0}'.format(USER_INPUT)
    except ValueError:  # Handle the Value Error
        print 'Error! only numbers are allowed'  # by printing out this
        break
