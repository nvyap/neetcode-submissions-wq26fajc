class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #char_index = {}
        max_len = 0
        res = []
        for ind,val in enumerate(s):
            #char_index[val] = ind
            if val not in res:
                res.append(val)
                l = len(res)
                max_len = max(max_len,l)
            else:
                i = res.index(val)
                res = res[i+1:]
                res.append(val)
        return max_len
        
            
        