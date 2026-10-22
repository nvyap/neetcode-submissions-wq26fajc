class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        i = 0
        while i<=l:
            if i not in nums:
                return i
            i += 1

        