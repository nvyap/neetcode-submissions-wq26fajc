class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        l = len(nums)
        
        for i in range(len(nums)):
            diff1 = 0-nums[i]
            j = i+1
            while j < l:
                diff2 = (diff1-nums[j])
                if diff2 in nums[j+1:]:
                    t = list([nums[i],nums[j],diff2])
                    if t not in result:
                        result.append(t)
                j += 1
        return result
