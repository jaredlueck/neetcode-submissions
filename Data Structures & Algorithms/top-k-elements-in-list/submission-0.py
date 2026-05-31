class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = dict()

        for num in nums:
            if not num in freq_dict:
                freq_dict[num] = 1
            else: 
                freq_dict[num] += 1
        
        entries = freq_dict.items()

        sorted_items = sorted(entries, key=lambda freq: freq[1], reverse=True)

        return [val[0] for val in sorted_items[:k]]