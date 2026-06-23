class TrieNode:
    def __init__(self, value = None):
        self.value = value
        self.children = {}

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        i = 0
        curr = self.root
        while i < len(word) and word[i] in curr.children:
            prev = curr
            curr = curr.children[word[i]]
            i += 1
        
        while i < len(word):
            node = TrieNode(word[i])
            curr.children[word[i]] = node
            curr = node
            i += 1
        curr.children['*'] = TrieNode('*')


    def search(self, word: str) -> bool:
        i = 0
        curr = self.root
        while i < len(word) and word[i] in curr.children:
            curr = curr.children[word[i]]
            i += 1
        print(i)
        return i == len(word) and '*' in curr.children
        

    def startsWith(self, prefix: str) -> bool:
        i = 0
        curr = self.root
        while i < len(prefix) and prefix[i] in curr.children:
            curr = curr.children[prefix[i]]
            i += 1
        return i == len(prefix)
        