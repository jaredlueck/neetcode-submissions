class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def valid_window(target, window):
            for i in range(len(target)):
                if window[i] != target[i]:
                    return False
            return True
        
        window = [0] * 26
        target = [0] * 26

        n = len(s2)
        m = len(s1)

        if m > n:
            return False
        
        for char in s1:
            val = ord(char) - ord('a')
            target[val] += 1
        l, r = 0, 0
        
        window[ord(s2[r]) - ord('a')] += 1
        
        while r < n:
            len_window = r - l + 1
            if len_window < m:
                r += 1
                if r < n:
                    window[ord(s2[r]) - ord('a')] += 1
            elif len_window > m:
                window[ord(s2[l]) - ord('a')] -= 1
                l += 1
            else:
                print(window)
                print(target)
                # window is the correct size
                if valid_window(target, window):
                    return True
                # window is not valid so try to take in another character
                r += 1
                if r < n:
                    window[ord(s2[r]) - ord('a')] += 1
        return False