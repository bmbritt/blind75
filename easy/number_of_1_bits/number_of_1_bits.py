class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        # this structure allows loop to run only for as many 1 bits exist
        while n:
            n = n - 1
            result += 1
        return result
        
        