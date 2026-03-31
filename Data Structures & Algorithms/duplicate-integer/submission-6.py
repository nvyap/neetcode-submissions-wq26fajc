class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = list(set(nums))
        return sorted(nums) != sorted(nums_set)
        