import string
import random
import pyinputplus as pyip

def createPassword(length=4, letters=True, Integers=False, Special_symb=False, ownSetOfSymb = False):
    charsForPassword = ''
    
    if isinstance(length,int) and length > 4:
        if not ownSetOfSymb:
            if isinstance(letters,bool) and True:
                charsForPassword += string.ascii_letters
            if isinstance(Integers,bool) and True:
                charsForPassword += string.digits
            if isinstance(Special_symb, str):
                charsForPassword += Special_symb
            return ''.join(random.choices(charsForPassword, k=length))
        else:
            if isinstance(ownSetOfSymb, str):
                charsForPassword = ownSetOfSymb
                return ''.join(random.choices(charsForPassword, k=length))
    else:
        return("Length is invalid")
    

print(createPassword(length=10, letters= True, Integers= True, Special_symb="!@#$%^&", ownSetOfSymb="!@#$%^dfghjs"))