class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        print(sorted_nums)
        n = len(nums)
        res = []
        i = 0
        while i < n:
            print(i)
            target = sorted_nums[i]
            j, k = i + 1, n - 1
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]: 
                i += 1
                continue
            while j < k:
                while j > i + 1 and j < n and sorted_nums[j] == sorted_nums[j-1]:
                    j += 1
                while k < n - 1 and k > 0 and sorted_nums[k] == sorted_nums[k+1]:
                    k -= 1
                if j >= k: break
                summ = sorted_nums[j] + sorted_nums[k]
                if summ + target == 0:
                    res.append([target, sorted_nums[j], sorted_nums[k]])
                    k -= 1
                    j = 1
                    continue
                elif summ + target > 0:
                    k -= 1
                else:
                    j += 1
            i += 1
                
        return res
