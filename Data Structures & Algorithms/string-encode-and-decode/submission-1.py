class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str = ""
        for i in strs:
            l = len(i)
            encode_str += str(l)+"#"+i
        return encode_str

    def decode(self, s: str) -> List[str]:
        #print(s)
        res = []
        n = 0
        while n<len(s):
            #print(n)
            j = n
            while s[j]!="#":
                j += 1
            
            #print(s[n:j])
            l1 = int(s[n:j])
            #print(l1)
            word = s[j+1:j+1+l1]
            res.append(word)
            n = j+l1
            n += 1

        return res


