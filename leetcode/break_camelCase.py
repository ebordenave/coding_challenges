# Complete the solution so that the function will break up camel casing, using a space between words.
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""

# loop through char in word, find capitalized char and add before capitalized char

def solution(s):
    new_str = ''
    for char in s:
        if char.isupper():
            new_str += ' ' + char
        else:
            new_str += char
    return new_str


solution('governmentYearFeelOwnCase')

# best solution
# def solution(s):
#     return ''.join(' ' + c if c.isupper() else c for c in s)

# note to self
# start with the thing you want to do and then provide a condition then everything else is one for one in s
# start backwards from for loop thinking
