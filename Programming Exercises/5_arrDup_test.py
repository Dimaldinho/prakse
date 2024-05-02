import random as r
import unittest
import time
start_time = time.time()

class TestCalculator(unittest.TestCase):
    def test_case(self):
        known_result = [([1, 1, 1, 1, 2, 2, 2], [1, 2]),
                ([1, 2, 3, 4, 5, 6], []),
                ([6, 6], [6])]
        
        
        for input,res in known_result:
            
            self.assertEqual(getArrDup(input),res)

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
    start_time = time.time()
    #unittest.main()

    #testArrDup()
    #arr = [1,2]
    #print(getArrDup(arr))
except customError as e:
    print("Custom Error:", e.message)
