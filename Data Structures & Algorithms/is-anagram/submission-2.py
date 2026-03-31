class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s_hm, t_hm = {}, {}
        for i in range(len(s)):
            s_hm[s[i]] = 1+s_hm.get(s[i],0)
            t_hm[t[i]] = 1+t_hm.get(t[i],0)
        for c in s:
            if s_hm[c]!= t_hm.get(c,0): 
                print(s_hm[c])
                print(t_hm.get(c,0))

                return False
        return True

        
    

            

        