#!/usr/bin/python

while True: # if the condition is True keep looping
    try: # Try this code if it has any error go to except condition
        print "Please input numbers only"  # print this
        answ = int(raw_input("INPUT > ")) #storing an input in a variable
        if answ != int(answ): # if the input is not an integer value 
            print "error! only numbers are allowed" # then print this
        else: # else
            print "your input is %i" %answ # print this
            break # and break out of the loop ( stop the looping )
    except ValueError: # Handle the Value Error
        print "Error! only numbers are allowed" # by printing out this 
