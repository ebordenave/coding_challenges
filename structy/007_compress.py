# def compress(s):
#     letters = 'abcdefghijklmnopqrstuvwxyz'
#     i = 0
#     j = 0
#     result = ''
    
#     while j <= len(s):
#         # print(j)
#         if s[j] in letters:
#             print(f'pointer is at a letter {s[j]}')
#             i = s[j]
#             result += i
#             j += 1
#     print(result)
#     return result
# s = 'aaa'
# compress(s)

def compress(s):
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

print(compress('ccaaatssss'))