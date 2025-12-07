class TrieNode:
    def __init__(self, val = None, end = False):
        self.val = val
        self.end = end
        self.children = {}

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode(c)
            node = node.children[c]
        node.end = True
            

    def search_helper(self, word, node):

        #check if it reached end val
        for i, c in enumerate(word):
            if i == len(word)-1:
                if c == ".":
                    for child in node.children.values():
                        if child.end == True:
                            return True
                    return False
                else:
                    if c not in node.children:
                        return False
                    else:
                        return node.children[c].end
                    
            else:
                if c == ".":
                    if node.children.values() == []:
                        return False

                    for child in node.children.values():
                        if self.search_helper(word[i+1:], child) == True: 
                            return True

                    return False
                else:
                    if c not in node.children:
                        return False
                
                node = node.children[c]
        #badder
        #bad.e.
        return True
    def search(self, word: str) -> bool:
        return self.search_helper(word, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)