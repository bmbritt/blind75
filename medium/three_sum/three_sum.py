class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
     
     result = []
     nums.sort()
     
     for i, num in enumerate(nums):
         
         # If already processed this number as start, proceed to next number
         if (i > 0 and num == nums[i-1]):
             continue
         # Impossible to add to 0 if smallest is > 0
         if (num > 0):
             break
         else: 
             left, right = i + 1, len(nums) - 1
             while (left < right):
                 sum = num + nums[left] + nums[right]
                 # sum too small, make bigger
                 if (sum < 0):
                     left += 1
                 # sum too big, make smaller
                 elif (sum > 0):
                     right -= 1  
                 else:
                     # triplet found
                     result.append([num, nums[left], nums[right]])
                     
                     # advance left or right until unique, will prevent duplicates
                     # unupdated one will update above because sum will become too large or too small
                     left += 1
                     while nums[left] == nums[left - 1] and left < right:
                         left += 1
     return result