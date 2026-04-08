class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = ""
        for i in s:
            if i.isalnum():
                clean_str += "".join(i.lower())
        
        return clean_str == clean_str[::-1]



        