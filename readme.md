Read:
1. Automate the boring stuff with Python: https://automatetheboringstuff.com/#toc 
2. https://learnpythontherightway.com/#read

WhatsApp Exercises:

1. Turtle_1.py:
    Based on https://learnpythontherightway.com/chapter/chapter-3.html
    In each step the turtle should move from 1 to 100 points in a random direction. The program that runs endlessly or until the point is more than 200 units away from the starting point.
2. Triangle_2.py 
    Create a function that receives the length of 3 triangle sides, and determine if a triangle can be formed. Return True if possible, False if not possible. 
3. passwordGenerator.py
    Create a password generator function, that takes parameters and returns a password that matches the requirements:
    * length # integer
    * letters=True/False # are letters allowed? If allowed, valid letters are Aa,Bb,Cc, ..., Zz
    * integers=True/False # are integers allowed? If they are, valid integers are 0,1,2,3,4,5,6,7,8,9
    * special_symbols = True/False # are special symbols allowed? If yes, decide which symbols should be allowed.
    * specify_all_characters=[]		# list of all allowed characters, for example, ["abcd123%^*&%"]. If this is specified, parameters letters, integers, and special_symbols are ignored.
4. ATM Simulator
    Description: The user starts with a certain account balance and can deposit, withdraw, or check the balance.
    * Ensure that the user cannot withdraw more than the current balance (print a warning message if this happens)
    * ATM only dispenses certain bill denominations ($5,10,20,50,100,500) (you can't withdraw $0.53, for example)