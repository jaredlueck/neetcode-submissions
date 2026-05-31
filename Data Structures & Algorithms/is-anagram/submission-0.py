class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        if n != m:
            return False
        
        ht_s = [0 for i in range(26)]
        ht_t = [0 for i in range(26)]

        for i in range(n):
            char_s = s[i]
            char_t = t[i]
            ht_s[ord(char_s) - 97] += 1
            ht_t[ord(char_t) - 97] += 1
        print(n)
        print(ht_s)
        print(ht_t)
        for i in range(26):
            if ht_s[i] != ht_t[i]:
                return False
        return True
