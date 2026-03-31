class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        top_k = c.most_common(k)
        return [item[0] for item in top_k]
        