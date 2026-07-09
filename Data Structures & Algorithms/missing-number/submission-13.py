class Solution:
    def missingNumber(self, nums: List[int]) -> int:        
        last = len(nums)
        l1 = max(nums)
        

        s = int(last*(last+1)/2)

        s1 = sum(nums)
        if len(nums) == l1 and s==s1:
            return 0

        print(s,s1)

        return (s-s1)

