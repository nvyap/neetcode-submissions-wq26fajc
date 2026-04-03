class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for ind,val in enumerate(nums):
            diff = target-val
            if diff in hm and hm[diff]!=ind:
                res = [hm[diff],ind]
            hm[val] = ind
        return res

        