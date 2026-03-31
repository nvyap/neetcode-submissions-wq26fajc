class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for ind in range(len(nums)):
            diff = target - nums[ind]
            if diff in hm:
                return [hm[diff],ind]
            hm[nums[ind]] = ind
        return []
