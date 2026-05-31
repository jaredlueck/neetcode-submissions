class Solution:
    def groupAnagrams(self, strs):
        groups = {}
        for s in strs:
            # Key for anagrams: sort the characters and join back into a string
            key = ''.join(sorted(s))
            if key in groups:
                groups[key].append(s)
            else:
                groups[key] = [s]
        return list(groups.values())