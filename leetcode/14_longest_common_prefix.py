# loop through list
# loop through the char in each string
# if the curr char is the same as the curr char of next string
# continue loop until not the same
# the chars that are the same

example = ["blight","blind","bluetooth"]

def longestCommonPrefix(strs: list[str]) -> str:
    res = ''
    
    for char in strs[0]:
        is_common = True
        for i in range(1, len(strs)):
            if char not in strs[i]:
                is_common = False
                break
        if is_common:
            res += char
    print(res)                        
    return res
    
    




longestCommonPrefix(example)


