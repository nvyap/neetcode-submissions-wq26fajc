class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_hash = {}
        for i in strs:
            s = [0]*26
            for j in i:
                o = ord(j)-ord('a')
                s[o] += 1
            s_tuple = tuple(s)
            if s_tuple not in result_hash:
                result_hash[s_tuple] = []
            result_hash[s_tuple].append(i)
        return list(result_hash.values())
        