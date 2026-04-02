class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        hm_rev = {}
        res = []
        for i in strs:
            hm[i] = "".join(sorted(i))
            if hm[i] not in hm_rev:
                hm_rev[hm[i]] = []
            hm_rev[hm[i]].append(i)
        
        print(hm_rev)

        for ind1,val1 in hm_rev.items():
            res.append(val1)

        return res






        

        