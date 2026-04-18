class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ""
        s2 = ""
        for i in s:
            if i.isalnum():
                s1 = s1+i.lower()
                s2 = i.lower()+s2
        return s1==s2