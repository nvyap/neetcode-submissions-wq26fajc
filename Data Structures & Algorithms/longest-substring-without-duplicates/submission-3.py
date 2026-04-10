class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        res = []
        for i in s:
            if i not in res:
                res.append(i)
                l = len(res)
                max_len = max(max_len,l)
            else: 
                ind = res.index(i)+1
                res = res[ind:]
                res.append(i)
        return max_len
        
            
        