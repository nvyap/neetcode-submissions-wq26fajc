class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hm = {}
        t_hm = {}
        if len(s)!=len(t): return False
        for i in range(len(s)):
            s_hm[s[i]] = 1+s_hm.get(s[i],0)
            t_hm[t[i]] = 1+t_hm.get(t[i],0)
        for j in s_hm:
            if s_hm[j] != t_hm.get(j,0): return False
        return True

        
        