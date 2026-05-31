class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        diff_map = dict()

        for i in range(n):
            val = nums[i]
            diff = target - val
            print(i)
            print(diff)
            print(diff_map)
            if diff in diff_map:
                return [diff_map[diff], i]
            if not diff_map.get(val):
                diff_map[val] = i
        
        return [0, 0]

        
                
