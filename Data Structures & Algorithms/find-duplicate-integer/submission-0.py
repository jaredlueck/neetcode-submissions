class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mapp = [False] * 10000

        for num in nums:
            if mapp[num]:
                return num
            mapp[num] = True
        return -1