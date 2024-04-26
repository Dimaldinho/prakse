
def romanToInt( s):
    """
    :type s: str
    :rtype: int
    """
    a = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    count =0
    p = 0
    for i in reversed(s):
        v = a[i]
        if v < p:
            count-=a[i]
        if v > p:
            count+=a[i]
        p = v
    
romanToInt(s="MCMXCIV")