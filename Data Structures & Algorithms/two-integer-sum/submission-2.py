class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return [k for k in range(len(nums)) if target-nums[k] in nums[:k]+nums[k+1:]]
        