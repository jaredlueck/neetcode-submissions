class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = [0] * len(nums)
        backward = [0] * len(nums)
        prev = 1
        for i in range(0, len(forward)):
            forward[i] = nums[i] * prev
            prev = forward[i]
        prev = 1
        for i in range(len(backward)-1, -1, -1):
            backward[i] = nums[i] * prev
            prev = backward[i]
        print(forward)
        print(backward)
        
        res = [0] * len(nums)
        for i in range(0, len(res)):
            left =  1 if i - 1 < 0 else forward[i-1]
            right = 1 if i + 1 >= len(res) else backward[i+1]
            res[i] = left * right
        return res