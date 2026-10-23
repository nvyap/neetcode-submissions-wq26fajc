class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for i in strs:
            s = [0]*26
            for j in i:
                o = ord(j) - ord('a')
                s[o] += 1
            s_tuple = tuple(s)
            if s_tuple not in hm:
                hm[s_tuple] = []
            hm[s_tuple].append(i)
        return list(hm.values())            

        