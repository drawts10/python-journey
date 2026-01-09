"""
Day of Knowledge: Building a calculator

Author:  Drawts

Description: Today, I am building a calculator with the knowledge I have gotten, I Though it could be done with this basic knowledge and 
yes, it is working so far, I have spent 2 hours and a half, I know it should have taken less, however I feel really great doing this, even
though it is taking too long, it is not officially finished but I need to take a quick rest, because I have done so many things today besidesthe calculator, I'm gonna share what I have done so far:

 - I have used the fabulous def get_positive_int to get the integer from the user and make the calculator useful.
 - As usual I am using conditions if/elif/else, however I'm stuck in this part, because it taking any others number as option which aren't, but I'm working on it now.
 - I have used a dictionary in order to attach the def of the functions created.
 - I created a function for the 4 main math operation, add, subtract, multiply and divide.
 - I have added a main function for the options sections to make the program start there.
 - I created two variables in order to ask the user for the numbers that wants on the operation like number a and number b.

 SECOND MODIFICATION:

 - After all, I made it :), I was having an issue with the condition that print the "option not available", I fixed it by placing the condiction right after the choice variable that ask to user to choose an option within the calculator, it worked 100% well. 
 - I added a ZeroDivisionError by making the loop in get_positive_int function ask for a number > 0. So now the program is not gonna crash if the user put a 0 as b number in divide function.
 - I added a "Exit" buttom so the user may end the program.
 - I am thinking about removing all those 4 printif statemets after a_number and b_number to make it better structurally using the ACTIONS dictionary. (I'm trying to figure out how to do it).
- I could condense the if statements using ACTIONS dictionary, by mapping the intenger keys direcly to function objects, I have eliminated the repetitive conditions and made the main function significantly easier to read and maintain.
- This code is pretty much better now, I'll update it later by learning more.

"""