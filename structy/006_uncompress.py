def uncompress(s):
    numbers = '0123456789'
    result = []
    
    # two variables that track indices
    i = 0
    j = 0
    
    # iterate to the length of the string
    while j < len(s):
        # moves the j pointer to characters
        if s[j] in numbers:
            j += 1
        else:
            # slice to capture a variable multidigit number
            num = int(s[i:j])
            # add this to the list- unique to python, a number times a char results in char num times
            result.append(num * s[j])
            # move the pointer again
            j += 1
            # catch up the i pointer to the j pointer
            i = j
            # join the results
    return result
            




print(uncompress("2c3a1t"))
            