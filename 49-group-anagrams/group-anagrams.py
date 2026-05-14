class Solution:
    #have a dictionary of sorted word being the key to a list of words
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = {}
        for word in strs:
            sorted_word = str(sorted(word))
            if sorted_word not in word_dict:
                word_dict[sorted_word] = []

            word_dict[sorted_word].append(word)
        return list(word_dict.values())
