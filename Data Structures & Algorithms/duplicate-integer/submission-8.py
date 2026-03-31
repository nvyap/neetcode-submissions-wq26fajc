class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = list(set(nums))
        return Counter(nums) != Counter(nums_set)
        