import turtle 
import random

wn = turtle.Screen()
alex = turtle.Turtle()
alex.pensize(3) 

while alex.distance(0,0) <=200: #distanceFromStart <= 200:
    alex.left(random.randint(0,360))
    alex.forward(random.randint(1,100))
    
wn.mainloop()