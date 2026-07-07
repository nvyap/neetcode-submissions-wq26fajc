class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        start = []
        longest = 0
        nums_set = set(nums)
        
        #if len(nums) == 0:
        #    return 0

        for i in nums_set:
            if i-1 not in nums_set:
                start.append(i)
        
        for j in start:
            k = j
            l = 0
            while k in nums_set:
                l += 1.
                k += 1
            if l > longest:
                longest = l
        
        return int(longest)


        