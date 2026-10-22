class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_hm = {}
        for s in strs:
            s_arr = [0]*26
            for j in s:
                ind = ord(j) - ord('a')
                s_arr[ind] += 1
            sarr_tuple = tuple(s_arr)
            if sarr_tuple not in str_hm:
                str_hm[sarr_tuple] = []
            
            str_hm[sarr_tuple].append(s)
        return list(str_hm.values())
        