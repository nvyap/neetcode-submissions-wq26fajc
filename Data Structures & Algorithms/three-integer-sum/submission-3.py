class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums_sort = sorted(nums)
        
        for i in range(len(nums_sort)):
            # Early exit: if first number is positive, no triplet sums to 0
            if nums_sort[i] > 0:
                break
            
            # Skip duplicate i values
            if i > 0 and nums_sort[i] == nums_sort[i - 1]:
                continue
            
            n1 = nums_sort[i] * -1
            j = i + 1
            k = len(nums_sort) - 1
            
            while j < k:
                current_sum = nums_sort[j] + nums_sort[k]
                if current_sum < n1:
                    j += 1
                elif current_sum > n1:
                    k -= 1
                else: 
                    res.append([nums_sort[i], nums_sort[j], nums_sort[k]])
                    # Skip duplicate j values
                    while j < k and nums_sort[j] == nums_sort[j + 1]:
                        j += 1
                    # Skip duplicate k values
                    while j < k and nums_sort[k] == nums_sort[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1

        return res