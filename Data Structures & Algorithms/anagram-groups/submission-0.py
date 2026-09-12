class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = {}
        for i in strs:
            c = sorted(i)
            key = "".join(sorted(c))
            if key not in s:
                s[key] =                               []                                 
                s[key].append(i)
            else:
                s[key].append(i)
        return list(s.values())