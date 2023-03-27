# loop through list
# loop through the char in each string
# if the curr char is the same as the curr char of next string
# continue loop until not the same
# the chars that are the same

example = ["blight","blind","bluetooth"]

def longestCommonPrefix(strs: list[str]) -> str:
    res = ''
    
    # iterate through first item in list
    for char in strs[0]:
        # instantiate a variable called is_common and assign the 'True' value to it
        is_common = True
        # iterate through the list starting at 1 (because len of a list is not zero indexed but range is)
        for i in range(1, len(strs)):
            # if that char in the first item is not in any of the strings, set is common to 'False' and then break out the loops
            if char not in strs[i]:
                is_common = False
                break
        # if is common remains true, instantiate a new variable called res and add the character to it
        # return the results
        if is_common:
            res += char
    print(res)                        
    return res
    
    




longestCommonPrefix(example)


