class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = ""
        self.refs = 0
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        curr = self.root
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                new_node = TrieNode()
                curr.children[c] = new_node
                curr = new_node
            curr.refs += 1
        curr.is_word = True
        curr.word = word
    
    def remove_word(self, word):
        curr = self.root
        for c in word:
            curr = curr.children[c]
            curr.refs -= 1

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = set()
        rows = len(board)
        cols = len(board[0])
        trie = Trie()
        def dfs(coord, visited, node):
            (row, col) = coord
            if node.refs == 0:
                return
            if node.is_word:
                res.add(node.word)
                trie.remove_word(node.word)
            for pos in [(-1 , 0), (1, 0), (0, -1), (0, 1)]:
                new_coord = (coord[0] + pos[0], coord[1] + pos[1])
                if new_coord[0] >= 0 and new_coord[0] < rows and new_coord[1] >= 0 and new_coord[1] < cols:
                    new_char = board[new_coord[0]][new_coord[1]]
                    if not new_coord in visited and new_char in node.children:
                        visited.add(new_coord)
                        dfs(new_coord, visited, node.children[new_char])
                        visited.remove(new_coord)
        
        
        for word in words:
            trie.add_word(word)

        for i in range(rows):
            for j in range(cols):
                if len(res) == len(words):
                    return list(res)
                if board[i][j] in trie.root.children:
                    dfs((i, j), {(i, j)}, trie.root.children[board[i][j]])
        return list(res)