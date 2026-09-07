"""
PYTHON SOLUTION - Min Stack
08/11/2026
TIME COMPLEXITY: O(1) for all operations (push, pop, top, getMin)
SPACE COMPLEXITY: O(N)
"""

##############
## SOLUTION ##
##############
class MinStack:
    
    ####################
    ## INIT           ##
    ####################
    def __init__(self):
        
        ####################
        ## MAIN SETUP     ##
        ####################
        # Use TWO stacks:
        #   1. self.stack -> holds the actual values (normal stack behavior)
        #   2. self.min_stack -> holds the MINIMUM seen so far at each point
        # Keeping them in sync (same length) lets getMin() be O(1) always,
        # since min_stack's top is always the current minimum.
        
        self.stack = []
        self.min_stack = []
    
    
    ####################
    ## PUSH           ##
    ####################
    def push(self, value: int) -> None:
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Always push onto the main stack
        self.stack.append(value)
        
        # Push onto min_stack the SMALLER of (value, current minimum)
        # If min_stack is empty, this new value IS the minimum by default
        if not self.min_stack:
            self.min_stack.append(value)
        else:
            self.min_stack.append(min(value, self.min_stack[-1]))
    
    
    ####################
    ## POP            ##
    ####################
    def pop(self) -> None:
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Pop from BOTH stacks together to keep them in sync
        self.stack.pop()
        self.min_stack.pop()
    
    
    ####################
    ## TOP            ##
    ####################
    def top(self) -> int:
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Simply return the last element of the main stack
        return self.stack[-1]
    
    
    ####################
    ## GET MIN        ##
    ####################
    def getMin(self) -> int:
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # The top of min_stack ALWAYS holds the current minimum
        return self.min_stack[-1]

#########
## EOF ##
#########

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()