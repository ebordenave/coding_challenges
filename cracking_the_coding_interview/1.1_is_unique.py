def is_unique(strs: str) -> bool:
    seen = set()
    
    for char in strs:
        if char in seen:
            return False
        seen.add(char)
    return True       

test_string = 'abcd'

print(is_unique(test_string))

# add the characters in set and as you iterate through
# if the current char exists in seen then return False, it is not unique
# else it will be True