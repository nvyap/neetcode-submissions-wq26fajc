class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        hm2 = {}
        res = []

        for i in range(len(nums)):
            hm[nums[i]] = hm.get(nums[i],0)+1
        
        for num,freq in hm.items():
            if freq not in hm2:
                hm2[freq] = []
            hm2[freq].append(num)
        
        for j in range(len(nums),0,-1):
            #print(j)
            if j in hm2 and len(res)<k:
                print(hm2[j])
                res = res+hm2[j]
        return res
