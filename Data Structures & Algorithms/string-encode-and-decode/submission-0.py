class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            for c in s:
                ascii_val = ord(c)
                res += str(ascii_val).zfill(3)
            res += "999"
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        cur = ""
        for i in range(0, len(s), 3):
            ascii_val = int(s[i:i + 3])
            if ascii_val == 999:
                res += [cur]
                cur = ""
            else:
                cur += chr(ascii_val)
        return res