import unittest
import time

def canConstruct(ransomenote, magazine):
    mag = {} 
    rnote = {}
    count = 0

    for char in magazine:
        if char not in mag:
            mag[char] = 1
        else:
            mag[char] += 1
    
    print(f"mag = {mag}")

    for char in ransomenote:
        if char not in rnote:
            rnote[char] = 1
        else:
            rnote[char] += 1
    
    print(f"rnote = {rnote}")
    
    if sorted(mag.items()) == sorted(rnote.items()):
        return sorted(mag.items()) == sorted(rnote.items())
    
    for char, charCount in mag.items():
        if char in rnote:
            if charCount >= rnote[char]:
                count +=1


    print(f"count = {count}")
    if count == len(rnote):
        return True
    else: return False
print(canConstruct(ransomenote="aa",magazine="aab"))