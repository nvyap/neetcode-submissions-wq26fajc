class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        last = len(nums)
        i = 0
        l1 = last-0+1

        if len(nums) == l1:
            return 0

        nums.sort()

        while i<=last:
            if i==last: return i
            
            if i != nums[i]: return i
            i += 1
            

        





        
        