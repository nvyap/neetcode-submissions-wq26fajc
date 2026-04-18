class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ""
        s2 = ""
        for i in s:
            if i.isalnum():
                s1 = s1+i.lower()
                s2 = i.lower()+s2
        l = len(s1)-1

        for j in range(len(s1)):
            if s1[j] != s2[j]:
                return False
        return True