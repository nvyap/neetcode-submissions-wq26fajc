class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,right = 0,len(nums)-1
        while left<right:
            mid = (right+left)//2
            if nums[right]<nums[mid]:
                left = mid+1
            elif nums[left]<nums[mid]:
                right = mid
            elif mid==left: return nums[mid]
            else: 
                left+=1
                right-=1

        return nums[left]
        