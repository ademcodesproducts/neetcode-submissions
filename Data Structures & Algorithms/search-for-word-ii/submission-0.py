class TrieNode:
    def __init__(self):
        self.children = {}
        self.isCompleteWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertTrie(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isCompleteWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        trie = Trie()

        for w in words:
            trie.insertTrie(w)

        len_row, len_col = len(board), len(board[0])

        allWords = set()
        visited = set()

        def dfs(r, c, node, word):

            if (
                r < 0 or
                c < 0 or
                r >= len_row or
                c >= len_col or
                (r, c) in visited or
                board[r][c] not in node.children
            ):
                return

            visited.add((r, c))

            node = node.children[board[r][c]]
            word += board[r][c]

            if node.isCompleteWord:
                allWords.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            visited.remove((r, c))

        for r in range(len_row):
            for c in range(len_col):
                dfs(r, c, trie.root, "")

        return list(allWords)