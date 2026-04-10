class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = ""
        for i in s:
            if i.isalnum():
                clean_str += "".join(i.lower())
        
        l = len(clean_str)
        for j in range(l):
            if clean_str[j] != clean_str[l-j-1]:
                return False
        return True



        