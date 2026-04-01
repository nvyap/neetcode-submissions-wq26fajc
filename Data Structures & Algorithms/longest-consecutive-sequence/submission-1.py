class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_ln = 0
        for i in nums:
            if i-1 not in num_set:
                curr_num = i
                curr_len = 1
                while curr_num+1 in num_set:
                    curr_num += 1
                    curr_len += 1
                max_ln = max(max_ln,curr_len)
        return max_ln
            
                

                    
