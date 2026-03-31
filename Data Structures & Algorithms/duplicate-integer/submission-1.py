class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l2 = list(set(nums))
        return (Counter(nums) != Counter(l2))
        