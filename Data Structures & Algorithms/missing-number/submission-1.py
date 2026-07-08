class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        first = min(nums)
        last = len(nums)
        i = 0
        l1 = last-first+1

        if len(nums) == l1:
            return 0

        full_list = []

        while i<=last:
            full_list.append(i)
            i += 1

        for j in full_list:
            if j not in nums:
                return j





        
        