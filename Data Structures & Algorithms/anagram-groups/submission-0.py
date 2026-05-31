class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ht = dict()

        for s in strs:
            sorted_s = str(sorted(s))
            if sorted_s in ht:
                ht[sorted_s].append(s)
            else:
                ht[sorted_s] = [s]
        res = []
        for k, v in ht.items():
            res.append(v)
        return res