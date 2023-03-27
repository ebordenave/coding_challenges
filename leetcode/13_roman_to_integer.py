
def romanToInt(s: str) -> int:
    # hashmap
    # map the symbols to the valuese
    # track the index of each symbol
    # if the current symbol is less than or equal to
    # the next number, the operation is subtraction with the next number
    # if the current number is greater than or equal the next number
    # then the operation is addition

    hashmap = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    print(len(s))
  
    res = 0
    print(range(len(s)))
    
    for idx in range(len(s)):
        if idx + 1 < len(s) and hashmap[s[idx]] < hashmap[s[idx+1]]:
            res -= hashmap[s[idx]]
        else:
            res += hashmap[s[idx]]
    return res



 
            
s='IV'
            
romanToInt(s)
        

