class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        #res = []

        for i in range(len(nums)):
            hm[nums[i]] = i
        for j,k in enumerate(nums):
            diff = target-k
            if diff in nums and hm[diff]!=j:
                return[j,hm[diff]]
        return []

        
        
        
        
        