class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, 0
        window = [0] * 26
        target = [0] * 26
        for char in s1:
            char_ord = ord(char) - ord('a')
            target[char_ord] += 1
        while r < len(s2):
            print(l,r)
            l_ord = ord(s2[l]) - ord('a')
            r_ord = ord(s2[r]) - ord('a')
            if not target[r_ord]:
                # this character is not in the permutation at all
                # so decreasing left pointer will not help
                while l <= r:
                    l_ord = ord(s2[l]) - ord('a')
                    window[l_ord] -= 1
                    l += 1
                r = l
            elif window[r_ord] == target[r_ord]:
                # character is in the permutation but we have too many,
                # so decrease the window until we have enough
                window[l_ord] -= 1
                l += 1
            else:
                window_len = r - l + 1
                if window_len == len(s1):
                    # we have found all the characters in the current substring
                    return True
                else:
                    # still need more characters
                    window[r_ord] += 1
                    r += 1
        return False