"""
PYTHON SOLUTION - Valid Parentheses
08/11/2026
TIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(N)
"""

##############
## SOLUTION ##
##############
class Solution:
    
    ####################
    ## IS VALID       ##
    ####################
    def isValid(self, s: str) -> bool:
        
        ####################
        ## EDGE CASE      ##
        ####################
        # An odd-length string can NEVER have perfectly matched brackets
        # (every open bracket needs exactly one matching close bracket)
        if len(s) % 2 != 0:
            return False
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Strategy: Stack-based matching
        # KEY INSIGHT: Brackets must close in LIFO (Last In, First Out) order -
        # this is EXACTLY what a stack naturally enforces!
        #
        # For each character:
        #   - If it's an OPENING bracket, push it onto the stack (we'll need
        #     to match it later)
        #   - If it's a CLOSING bracket, check if it matches the bracket
        #     currently on TOP of the stack. If yes, pop it (successfully
        #     matched). If no (wrong type OR stack is empty), the string
        #     is invalid immediately.
        #
        # At the end, if the stack is EMPTY, every bracket was matched.
        # If anything remains, some open bracket was never closed.
        
        # Map each closing bracket to its corresponding opening bracket
        matching_pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        
        stack = []
        
        for char in s:
            if char in matching_pairs:
                # This is a CLOSING bracket - check for a valid match
                # Pop the top of stack if it exists, otherwise use a
                # placeholder that can never match (handles empty stack safely)
                top_element = stack.pop() if stack else '#'
                
                if matching_pairs[char] != top_element:
                    return False
            else:
                # This is an OPENING bracket - push it for later matching
                stack.append(char)
        
        # Valid only if ALL brackets were successfully matched and popped
        return len(stack) == 0

#########
## EOF ##
#########