class Solution:
    def countBits(self, n: int) -> List[int]:
        
        # just getting the hamming weight of each integer in range [0, n]
        # check out number_of_1_bits or kernighan's algorithm
        
        # result = [0] * (n+1)
        # for i in range(n + 1):
            
        #     while (i):
        #         i &= (i - 1)
        #         result[i] += 1
        # return result
        
        # Dynamic programming
        result = [0] * (n+1)
        offset = 1
        
        for i in range(1, n + 1):
            
            if (offset * 2 == i):
                offset *= 2
            result[i] = 1 + result[i - offset]
        return result
            
        
        
        