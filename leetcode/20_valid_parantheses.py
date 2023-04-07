class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # Initialize an empty stack to keep track of opening brackets
        closeToOpen = {')':'(',']':'[','}':'{'}  # Define a mapping of closing brackets to their opening counterparts

        for char in s:  # Loop through each character in the input string
            if char in closeToOpen:  # If the character is a closing bracket
                if stack and stack[-1] == closeToOpen[char]:  # If the stack is not empty and the top of the stack matches the corresponding opening bracket
                    stack.pop()  # Remove the opening bracket from the stack
                else:
                    return False  # If the stack is empty or the top of the stack does not match the corresponding opening bracket, the input string is invalid
            else:
                stack.append(char)  # If the character is an opening bracket, add it to the stack

        return True if not stack else False  # If the stack is empty, the input string is valid; otherwise, it is invalid
