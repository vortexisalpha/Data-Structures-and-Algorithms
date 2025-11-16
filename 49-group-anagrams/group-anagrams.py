class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for s in strs:
            s_map = collections.Counter(s)
            s_set = frozenset(s_map.items())

            if s_set not in dic:
                dic[s_set] = [s]
            else:
                dic[s_set].append(s)

        return list(dic.values())

