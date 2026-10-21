class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        hm = {}
    

        for i in range(len(nums)):
            d = target - nums[i]
            if d in hm:
                return [hm[d],i]
            else:
                hm[nums[i]] = i
        return []
        