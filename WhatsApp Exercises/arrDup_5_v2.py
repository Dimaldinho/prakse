import random as r

dupl = []
class customError(Exception):
    def __init__(self, message):
        self.message = message



def testArrDup():
    testArr = []
    for i in range(10):
        testArr.append(r.randint(0,50))
    print(testArr)
    print(getArrDup(testArr))
    

def getArrDup(arr):
    if not isinstance(arr, list) or len(arr)<2  or not all(isinstance(item,int) for item in arr):
        raise customError("Wrong arr")
    
    freq = {}
    dupl = []

    for i in arr:
        if i not in freq:
            freq[i] = 1
        else: 
            freq[i] += 1
    
    
    for i, count in freq.items():
        if count > 1:
            dupl.append(i)
    
    print(freq)
    return dupl

try:
    testArrDup()
    #arr = [1,2]
    #print(getArrDup(arr))
except customError as e:
    print("Custom Error:", e.message)
