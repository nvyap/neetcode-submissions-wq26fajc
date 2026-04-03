class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        hm_rev = {}
        for i in strs:
            sort_str = "".join(sorted(i))
            hm[i] = sort_str
            if sort_str not in hm_rev:
                hm_rev[sort_str] = []
            hm_rev[sort_str].append(i)           

        return list(hm_rev.values())


        
        