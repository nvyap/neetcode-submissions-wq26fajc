class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        start = []

        for i in nums:
            if i-1 not in nums:
                start.append(i)


        for j in start:
            l = 1
            j += 1
            while j in nums:
                l += 1
                j += 1
            max_len = max(max_len,l)
        return max_len

                     
        
                
            

        