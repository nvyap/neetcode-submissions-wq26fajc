class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        l = len(nums)
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            diff1 = 0-nums[i]
            left = i + 1
            right = l - 1
            while left < right:
                total = nums[left] + nums[right]
                if total == diff1:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < diff1:
                    left += 1
                else:
                    right -= 1
        return result
