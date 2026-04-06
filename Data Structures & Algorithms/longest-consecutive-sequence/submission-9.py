class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        start = []
        nums_set = set(nums)

        for i in nums_set:
            if i-1 not in nums:
                start.append(i)


        for j in start:
            l = 1
            j += 1
            while j in nums_set:
                l += 1
                j += 1
            max_len = max(max_len,l)
        return max_len

                     
        
                
            

        