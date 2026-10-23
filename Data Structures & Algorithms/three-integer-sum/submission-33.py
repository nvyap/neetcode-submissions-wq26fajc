class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ln = len(nums)-1
        result = []

        for i,n in enumerate(nums):
            if n > 0:
                break
            if i>0 and n == nums[i-1]:
                continue
            diff = 0-n
            l = i+1
            r = ln
            
            while l<r:
                s = nums[l]+nums[r]
                if s==diff:
                    result.append([n,nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l<r and nums[l] == nums[l-1]:
                        l += 1
                    
                elif s<diff:
                    l += 1
                else: r -= 1
        return result



        