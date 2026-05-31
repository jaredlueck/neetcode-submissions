class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ht = set()

        for num in nums:
            if num in ht:
                return True
            ht.add(num)
        return False