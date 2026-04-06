class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        res = []
        for i in strs:
            sort_i = "".join(sorted(i))
            if sort_i not in hm:
                hm[sort_i] = []
            hm[sort_i].append(i)
        
        for ind,val in hm.items():
            res.append(val)

        return res
        