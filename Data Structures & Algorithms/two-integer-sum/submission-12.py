class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i in range(len(nums)):
            hm[nums[i]] = i
        for j in range(len(nums)):
            diff = target-nums[j]
            if diff in hm and hm[diff]!=j:
                return [j,hm[diff]]
        return []
        
        
        
        
        