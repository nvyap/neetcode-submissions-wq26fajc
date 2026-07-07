class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        nums_set = set(nums)
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in hm:
                return [hm[diff],i]
            hm[nums[i]] = i
        return []


            
        