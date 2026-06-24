class Solution:
    def minWindow(self, s: str, t: str) -> str:        
        window = {}

        for char in t:
            window[char] = window.get(char, 0) + 1

        # cnt is the number of unique characters in the window
        cnt = len(window)
        res = [-1, -1]
        resLen = float('inf')
        l = 0
        # increasing the right pointer brings more characters into the window
        for r in range(len(s)):
            print(cnt)
            if s[r] in window:
                window[s[r]] -= 1
                if window[s[r]] == 0:
                    cnt -= 1

            # the current window contains all the characters
            # so try to shrink it by increasing the left pointer
            while cnt == 0:
                if resLen > r - l + 1:
                    res = [l, r]
                    resLen = r - l + 1
                if s[l] in window:
                    window[s[l]] += 1
                    if window[s[l]] > 0:
                        cnt += 1
                l += 1

        return "" if resLen == float('inf') else s[res[0]:res[1]+1]
                

            

