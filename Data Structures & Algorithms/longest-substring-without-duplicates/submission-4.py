class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        char_map = {}
        n = len(s)
        l, r = 0, 0
        char_map[s[r]] = 0
        max_substring = 1
        while r < n - 1:
            # extend the window by 1
            r += 1
            # we have already seen this character so shrink the window
            if char_map.get(s[r], -1) >= l:
                l = char_map[s[r]] + 1
            char_map[s[r]] = r
            max_substring = max(max_substring, r - l + 1)
        return max_substring

