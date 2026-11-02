class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        i = 0
        hm = {}
        for j,n in enumerate(nums):
            hm[n] = j
        while i<=l:
            if i not in hm:
                return i
            i += 1

        