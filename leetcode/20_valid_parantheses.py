class Solution:
    def isValid(self, s: str) -> bool:
        # a stack is an array, think of it vertically like a pringles can full of chips
        stack = []
        # use a dictionary here as a way to identify valid parantheses
        open_to_close = {')':'(','}':'{',']':'['}
        # iterate through the string, looking for characters
        for char in s:
            # in the first iteration, the char will not be in this string, in the second iteration it will be
            # when it is, if the stack is not empty and the item at the top of the stack equals that same character in open_to_close
            # pop that pringle can
            if char in open_to_close:
                if stack and stack[-1] == open_to_close[char]:
                    stack.pop()
                else:
                    # if it is not in there, then it is not valid and so you return False
                    return False
            else:
                # go back to first conditional, this will begin adding the chars into the stack
                stack.append(char)
        # return if the stack is empty, if it is not then return False
        return True if not stack else False

