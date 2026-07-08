class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        first = min(nums)
        last = len(nums)
        i = 0
        l1 = last-first+1

        if len(nums) == l1:
            return 0

        while i<=last:
            if i not in nums: return i
            i += 1
            

        





        
        