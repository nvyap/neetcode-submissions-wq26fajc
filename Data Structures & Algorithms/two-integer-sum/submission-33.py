class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i,val in enumerate(nums):
            diff = target-val
            if diff in hm and hm[diff]!=i:
                print(hm.get(diff,-1))
                return [hm[diff],i]
            hm[val] = i
        
        return []
        