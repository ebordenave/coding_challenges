
def isPalindrome(s: str) -> bool:
    # left starts at beginning of s and right starts at the end         
    left, right = 0, len(s) - 1
    # While left is still before right        
    while left < right:
        # If left is not in alpha-numeric character then advance i            
        if not s[left].isalnum():
            left += 1
        # If right is not in alpha-numeric character then advance i
        elif not s[right].isalnum():
            right -= 1
        # Both left and right are alpha-numeric characters at this point so if they do not match return the fact that input was non-palindrom
        elif s[left].lower() != s[right].lower():
            return False
        # Otherwise characters matched and we should look at the next pair of characters
        else:
            left, right = left + 1, right - 1
    # The entire string was verified and we return the fact that the input string was palendrom      
    return True


s = 'A man, a plan, a canal: Panama'

isPalindrome(s)