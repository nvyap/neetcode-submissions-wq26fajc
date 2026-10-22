class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_l = 0
        hs = set()
        ind = 0
        for i in s:
            
            while i in hs:
                hs.remove(s[ind])
                ind += 1
            hs.add(i)
            max_l = max(max_l,len(hs))
        return max_l
        