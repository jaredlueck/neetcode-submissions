class Solution:
    def isChar(self, c: str):
        ascii_val = ord(c)
        return (ascii_val >= 48 and ascii_val <= 57) or (ascii_val >= 65 and ascii_val <= 90) or (ascii_val >= 97 and ascii_val <= 122)
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1

        while i < j:
          while i < j and not self.isChar(s[j]): j -= 1
          while i < j and not self.isChar(s[i]): i += 1
          if i >= j:
            break
          if s[i].lower() != s[j].lower():
            print(s[i])
            print(s[j]) 
            return False
          i += 1
          j -= 1
        return True