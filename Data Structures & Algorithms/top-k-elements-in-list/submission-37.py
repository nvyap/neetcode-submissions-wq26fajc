class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        count_rev = {}
        res = []
        for i in nums:
            count[i] = count.get(i,0)+1
        
        for ind,val in count.items():
            if val not in count_rev:
                count_rev[val] = []
            count_rev[val].append(ind)
        
        for j in range(len(nums),0,-1):
            if j in count_rev and len(res)<k:
                res.extend(count_rev[j])

        return res


        



        