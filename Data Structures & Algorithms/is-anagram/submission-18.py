class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hm_s, hm_t = {},{}
        for j in range(len(s)):
            hm_s[s[j]] = hm_s.get(s[j],0)+1
            hm_t[t[j]] = hm_t.get(t[j],0)+1
        for k in range(len(hm_s)):
            if hm_s[s[k]] != hm_t.get(s[k],0):
                return False
        return True
        
        

            
        