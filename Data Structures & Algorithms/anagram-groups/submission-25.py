class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_hash = {}
        for i in strs:
            s = [0]*26
            for j in i:
                o = ord(j)-ord('a')
                s[o] += 1
            s_tuple = tuple(s)
            if s_tuple not in strs_hash:
                strs_hash[s_tuple] = []
            strs_hash[s_tuple].append(i)
        return list(strs_hash.values())