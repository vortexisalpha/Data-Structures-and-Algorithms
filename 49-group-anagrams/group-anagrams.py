from collections import Counter, defaultdict
class Solution:
    #have a dictionary of sorted word being the key to a list of words
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def hash_gen(s):
            char_list = [0] * 26
            for c in s:
                char_list[ord(c)- ord("a")] += 1
            return tuple(char_list)


        sol = defaultdict(list)
        for s in strs:
            sol[hash_gen(s)].append(s)

        return list(sol.values())
