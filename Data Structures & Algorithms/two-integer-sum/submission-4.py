class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        op = []
        for i in range(len(nums)):
            if target-nums[i] in nums[:i]+nums[i+1:]:
                op.append(i)
        return op

        