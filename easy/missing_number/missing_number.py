class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # result = len(nums)
        
        # for i, num in enumerate(nums):
        #     # take a pair of values (1 from full set, 1 from array) and xor them
        #     # if they are equal (which they will be in all but 1 case),
        #     # it will result in 0 being XORed with result which will leave it unchanged
        #     pairXOR = i ^ nums
        #     result ^= pairXOR
        # return result
        rangeSum = len(nums) * (len(nums) + 1) // 2
        return rangeSum - sum(nums)
        
        
       
       