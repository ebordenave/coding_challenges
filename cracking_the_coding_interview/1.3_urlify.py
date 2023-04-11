def urlify(strs:str) -> str:
    new_strs = ''
    
    for char in strs:
        if char == ' ':
            new_strs += '%20%'
        else:
            new_strs += char
    return new_strs

test_string = 'Mr John Smith'

print(urlify(test_string))

