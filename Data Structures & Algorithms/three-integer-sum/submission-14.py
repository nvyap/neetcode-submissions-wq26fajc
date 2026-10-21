class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1
            diff = 0-nums[i]
            while l<r:
                if nums[l]+nums[r] == diff and [nums[i],nums[l],nums[r]] not in result:
                    result.append([nums[i],nums[l],nums[r]])
                    l += 1
                    continue
                elif nums[l]+nums[r] <diff:
                    l += 1
                    continue
                else:
                    r -= 1
                    continue

        return result
                

                


        