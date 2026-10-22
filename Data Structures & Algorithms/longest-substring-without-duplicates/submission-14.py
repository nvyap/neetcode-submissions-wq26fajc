class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hs = set()
        max_len = 0
        l = 0

        for i in s:
            
            while i in hs:
                hs.remove(s[l])
                l += 1
            hs.add(i)
            ln = len(hs)
            max_len = max(ln,max_len)
        return max_len
        