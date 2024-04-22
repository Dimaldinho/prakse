
spam = ['apples', 'bananas', 'tofu', 'cats']
newStr = ""
def CommaCode(my_list):
    if len(my_list) != 0:
        newStr = ""
        for i in range(len(my_list)-1):
            newStr += my_list[i]
            if i != len(my_list)-2:
                newStr += ", "
        newStr += ' and ' + my_list[-1] 
        print(newStr)

CommaCode(spam)