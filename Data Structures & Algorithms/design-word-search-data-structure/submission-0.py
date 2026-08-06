class TrieNode:
    def __init__(self):
        self.children = {}
        self.isCompleteWord = False

class WordDictionary:

    def __init__(self):
        self.node = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.node
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isCompleteWord = True

    def search(self, word: str) -> bool:

        def dfs(i, node):
            curr = node
            if i == len(word):
                return node.isCompleteWord

            c = word[i]
            if c == ".":
                for child in curr.children.values():
                    if dfs(i+1, child):
                        return True
                return False
            else:
                if c not in curr.children:
                    return False
            curr = curr.children[c]
            return dfs(i+1, curr)

        return dfs(0, self.node)