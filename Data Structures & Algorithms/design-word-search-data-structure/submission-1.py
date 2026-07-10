class TrieNode:
    def __init__(self, val: str):
        self.val = val
        self.children = {}


class WordDictionary:

    def __init__(self):
        self.root = TrieNode("")

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                new_node = TrieNode(char)
                curr.children[char] = new_node
                curr = new_node
        terminate_node = TrieNode("*")
        curr.children["*"] = terminate_node

    def search(self, word: str) -> bool:
        # traverse will search for a subtree for a word
        def traverse(root, word):
            curr = root
            for i, char in enumerate(word):
                if char == ".":
                    # for wildcard we should recursively try all the subtrees
                    for child in curr.children.values():
                        found = traverse(child, word[i+1:])
                        if found:
                            # we were able to match the word in one of the subtrees
                            return True
                    # could not match the word in any of the subtrees
                    return False
                elif char not in curr.children:
                    # word is not in the tree
                    return False
                else:
                    # keep traversing the tree
                    curr = curr.children[char]
            return '*' in curr.children
        
        return traverse(self.root, word)

