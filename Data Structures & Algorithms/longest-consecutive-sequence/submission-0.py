class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        # longest sequence starting from this number
        m_start = {}
        # longest sequence ending from this number
        m_end = {}
        for num in nums:
            if num in m_start:
                continue
            # current longest sequence up to num - 1
            prev = m_end.get(num - 1, 0)
            nxt = m_start.get(num + 1, 0)

            m_start[num] = 1 + nxt
            m_end[num] = 1 + prev
            
            if prev > 0: 
                m_start[num - prev] = m_start.get(num - prev,0) + nxt + 1
            if nxt > 0:
                m_end[num + nxt] = m_end.get(num + nxt, 0) + prev + 1

        return max(m_start.values())
