from collections import defaultdict
class Solution:
    #have a dictionary of sorted word being the key to a list of words
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        solution = defaultdict(list)
        for s in strs:
            solution[str(sorted(s))].append(s)
        return list(solution.values())