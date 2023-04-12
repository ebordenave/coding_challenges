def string_compression(s: str) -> str:
    s += '!'
    result = ''
    i = 0
    j = 0
    
    while j < len(s):
        # find a streak of consecutive char
        if s[i] == s[j]:
            j += 1
        else:
            num = j - i
            
            if num == 1:
                result += s[i]
            else:
                result += str(num) + s[i]
            i = j
    return result

test = 'aababacca'


print(string_compression(test))