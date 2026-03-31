class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        hm_ind = {}
        for i in range(len(nums)):
            hm[nums[i]] = i
        for ind,val in enumerate(nums):
            diff = target-val
            if diff in nums and hm[diff]!=ind:
                return [ind,hm[diff]]
        return []
        
        
        
        
        