class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = ""
        for i in s:
            if i.isalnum():
                clean_str += "".join(i.lower())

        print(clean_str)
        print(clean_str[::-1])
        
        return clean_str == clean_str[::-1]



        