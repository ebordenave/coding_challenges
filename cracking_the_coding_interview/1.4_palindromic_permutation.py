from collections import defaultdict


def is_palindromic_permutation(strs:str) -> bool:
    strs = strs.lower()
    counter = defaultdict(int)
    
    for char in strs:
        if ord(char) >= 97 and ord(char) <= 122:
            counter[char] += 1

    middle_char = ""  # initializing variable to hold the middle_char character
    for letter in counter:  # iterating through the characters in the counter dictionary
        if middle_char and counter[letter] % 2 == 1:  
            # if middle_char already has a value and the current letter has an odd count, the string cannot be rearranged to form a palindrome, so return False
            return False
        elif counter[letter] % 2 == 1:
            # if the current letter has an odd count, assign it to the middle_char variable
            middle_char = letter
    return True  # if all characters have even counts or a middle_char character has been assigned, the string can be rearranged to form a palindrome, so return True.


def is_permutation(strs_one: str,strs_two: str) -> bool:
    count_one, count_two = {},{}
    
    if len(strs_one) != len(strs_two):
        return False
    
    for idx in range(len(strs_one)):
        count_one[strs_one[idx]] = 1 + count_one.get(strs_one[idx], 0)
        count_two[strs_two[idx]] = 1 + count_two.get(strs_two[idx], 0)
    return count_one == count_two


ex_one = 'Tact Coa'

print(is_palindromic_permutation(ex_one))