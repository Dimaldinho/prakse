import pyinputplus as pyip
import string
t = []

def getSides(triangle):
    for i in range(3):
        triangle.append(pyip.inputInt("Input %s side of a triangle \n" %(i+1)))

def checkIfPossible(triangleSides):
    if isinstance(triangleSides, list) and len(triangleSides) == 3:
        for item in triangleSides:
            if not isinstance(item, int):
                print("Incorrect Data")
                return False
        
    
        if triangleSides[0] + triangleSides[1]>triangleSides[2] and \
        triangleSides[0] + triangleSides[2]>triangleSides[1] and\
        triangleSides[1] + triangleSides[2]>triangleSides[0]:
            return True
        else: return False
    else: return False
    
getSides(t)
print("Triangle sides: " + str(t))
print(checkIfPossible(t))

