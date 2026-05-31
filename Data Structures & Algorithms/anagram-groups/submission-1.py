class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = dict()
        res = []
        for s in strs:
            ss = "".join(sorted(s))
            if not ss in anagrams_dict:
                anagrams_dict[ss] = [s]
            else:
                anagrams_dict[ss].append(s)
        
        for k, v in anagrams_dict.items():
            res.append(v)
        return res
