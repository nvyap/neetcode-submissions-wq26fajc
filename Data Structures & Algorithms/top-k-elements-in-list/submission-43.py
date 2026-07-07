class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm_nums = {}
        hm_rev = defaultdict()
        res = []
        l = len(nums)
        for i in nums:
            hm_nums[i] = hm_nums.get(i,0)+1

        for j in hm_nums:
            if hm_nums[j] not in hm_rev:
                hm_rev[hm_nums[j]] = []
            hm_rev[hm_nums[j]].append(j)
        for n in range(len(nums),0,-1):
            if n in hm_rev:
                res.extend(hm_rev[n])
        return res[:k]

        