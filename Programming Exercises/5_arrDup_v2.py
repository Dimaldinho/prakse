import random as r
import unittest
import time

dupl = []
class customError(Exception):
    def __init__(self, message):
        self.message = message



def testArrDup():
    testArr = []
    for i in range(5000):
        testArr.append(r.randint(0,50))
    print(testArr)
    print(getArrDup(testArr))
    

def getArrDup(arr):
    if not isinstance(arr, list) or len(arr)<2  or not all(isinstance(item,int) for item in arr):
        raise customError("Wrong arr")
    
    freq = {}
    dupl = []
    count = 0
    for i in arr:
        if i not in freq:
            freq[i] = 1
        else: 
            freq[i] += 1
    
    
    for i, count in freq.items():
        if count > 1:
            dupl.append(i)
    return dupl
    

    
    
    # count = 0
    # for n in arr:
    #     if n == all(dupl):
    #         count += 1
    # return count > 1

    # return dupl

try:
    
    #test_cases = [[1,3,5,6,8,4,3,6,6],{6,3}]
    
    #if getArrDup(test_cases[0]) == list(test_cases[1]):
    #    print("Ok")
    start_time = time.time()
    testArrDup()
    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time:",execution_time)
    #testArrDup()
    #arr = [1,2]
    #print(getArrDup(arr))
except customError as e:
    print("Custom Error:", e.message)
