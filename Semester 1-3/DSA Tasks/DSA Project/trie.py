class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word.lower():
            node = node.children.setdefault(char, TrieNode())
        node.is_end_of_word = True

    def autocomplete(self, prefix):
        results = []
        node = self.root
        for char in prefix.lower():
            if char not in node.children:
                return results
            node = node.children[char]
        self._dfs(node, prefix.lower(), results)
        return results

    def _dfs(self, node, prefix, results):
        if node.is_end_of_word:
            results.append(prefix)
        for char, next_node in node.children.items():
            self._dfs(next_node, prefix + char, results)
