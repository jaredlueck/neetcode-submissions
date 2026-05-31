class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # window must satisfy count( i s.t. s[i] != C ) < k
        # must maximize window size = r - l + 1
        # find C that maximizes window size
        char_counts = defaultdict(int)
        maxf = 0
        l = 0
        res = 0
        for r in range(len(s)):
            char_counts[s[r]] += 1
            maxf = max(maxf, char_counts[s[r]])
            
            while (r - l + 1) - maxf > k:
                
                char_counts[s[l]] -= 1
                l += 1
            res = max(res, (r-l +1))
        return res
