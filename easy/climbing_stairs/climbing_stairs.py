class Solution:
    def climbStairs(self, n: int) -> int:
        
        result = 1
        addend = 0
        for i in range(1, n+1):
            tmp = result
            result += addend
            addend = tmp
            
        return result
        # possibilities = {
        #     1 : 1,
        #     2 : 2
        # }
        
        # for i in range(1, n+1):
        #     if (i not in possibilities):
        #         possibilities[i] = possibilities[i-1] + possibilities[i - 2] 
        # return possibilities[n]