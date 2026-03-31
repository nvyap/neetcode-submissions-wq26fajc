class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return [k for k in range(len(nums)) if target-nums[k] in nums[:k]+nums[k+1:]]
        '''
        for i in range(len(nums)):
            

            new_list = nums[:i] + nums[i+1:]
            j = target-nums[i]
            if j in new_list:
                ind = [i for i, val in enumerate(nums) if val == target]
                return [i,ind]
            '''
            


        