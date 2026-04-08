class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        
        for i in range(len(nums)):
            addendTarget = target - nums[i]
            if (addendTarget in map):
                return [map[addendTarget], i]
            else:
                map[nums[i]] = i