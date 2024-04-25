import random as r

dupl = []
class customError(Exception):
    def __init__(self, message):
        self.message = message



def testArrDup():
    testArr = []
    for i in range(50000):
        testArr.append(r.randint(0,9))
    print(testArr)
    print(getArrDup(testArr))

def getArrDup(arr):
    if not isinstance(arr, list) or len(arr)<2  or not all(isinstance(item,int) for item in arr):
        raise customError("Wrong arr")
    
    
    for i in range(len(arr)):
        if i == 1000:
            print("aaaaaaaa")
        for j in range(i+1,len(arr)):
            flag = False
            if arr[i] == arr[j]:
                for y in range(len(dupl)):
                    if dupl[y] == arr[i]:
                        flag = True
                        break
                if not flag:
                    flag = False
                    dupl.append(arr[i])
    
    return dupl

try:
    testArrDup()
    #arr = [1,2]
    #print(getArrDup(arr))
except customError as e:
    print("Custom Error:", e.message)
