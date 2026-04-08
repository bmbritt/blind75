class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        
        stack = []
        
        for char in s:
            if (char in pairs):
                # cannot add close to an empty stack
                if (stack and pairs[char] == stack[-1]):
                    stack.pop()
                # close doesnt match the open
                else:
                    return False
            # add the opening bracket
            else:
                stack.append(char)
        # stack will be empty if valid, not empty if there were opening brackets that were never closed 
        return not stack