import string
import random
import pyinputplus as pyip

#print(string.ascii_letters)
#print(string.digits)
def createPassword(length, specs):
    charsForPassword = ''
    if isinstance(specs, str):
        charsForPassword = specs
    if isinstance(specs, list):
        if specs[0]:
            charsForPassword += string.ascii_letters
        if specs[1]:
            charsForPassword += string.digits
        if specs[2]:
            charsForPassword += specs[2]

    return ''.join(random.choices(charsForPassword, k=length))

    
#    if isinstance(specs, str):
#        return print(''.join(random.choices(specs, k=length)))
#    elif(isinstance(specs, list)):
#        if     
def createSpecifications():
    specs=[]
    length = pyip.inputInt('How many chars? \n', min=4)
    specify_all_characters= pyip.inputStr('Specify your own symbols \n',blank = True)
    if specify_all_characters:
        return length, specify_all_characters
    
    specs.append(pyip.inputBool('Letters? (True/False): \n'))
    specs.append(pyip.inputBool('Integers? (True/False): \n'))
    specs.append(pyip.inputBool('Special symbols? (True/False): \n'))
    if specs[-1]:
        specs[-1] = (pyip.inputRegexStr(prompt= 'Specify your own symbols ',allowRegexes=[r'[!@#$%^&*()_+\-=[\]{}|;:,.<>?]']))
    #specify_all_characters= pyip.inputStr('Specify your own symbols \n',blank = True)
    
    return length, specs


length, specifications = createSpecifications()
print(createPassword(length, specifications))