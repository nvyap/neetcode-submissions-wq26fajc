class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hash_set_t = {}
        hash_set_s = {}
        for i in range(len(s)):
            hash_set_s[s[i]] = 1+hash_set_s.get(s[i],0)
            hash_set_t[t[i]] = 1+hash_set_t.get(t[i],0)
        
        for j in hash_set_s:
            if hash_set_s[j] != hash_set_t.get(j,0):
                return False
        return True


            
        