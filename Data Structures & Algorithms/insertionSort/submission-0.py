# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        j = 0
        res = []
        
        while j < len(pairs):
            temp = j-1
            while temp>=0  and pairs[temp].key > pairs[temp+1].key:
                pairs[temp],pairs[temp+1] = pairs[temp+1],pairs[temp]
                temp -= 1
            r1 = list(pairs)
            res.append(r1)
            j += 1
            
        return res

        
        