def findLongestPref(strs):
    s = min(strs,key=len)

    
    for i, char in enumerate(s):
        
        for string in strs:
            
            if string[i] != char:
                return s[:i]

    print(s[::-1])
    
    return s


print(findLongestPref(strs= ["abaaaa","abaaaa","abaaaaaa"]))