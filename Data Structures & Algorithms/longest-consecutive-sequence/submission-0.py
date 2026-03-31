class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_ln = 0
        for i in nums:
            if i-1 not in num_set:
                current_num = i
                current_len = 1
                while current_num+1 in num_set:
                    current_num += 1
                    current_len += 1
                max_ln = max(max_ln,current_len)
        return max_ln
                    
