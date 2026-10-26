class PrefixTree:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node["$"] = True

    def search(self, word: str) -> bool:
        node = self._find(word)
        return node is not None and "$" in node

    def startsWith(self, prefix: str) -> bool:
        return self._find(prefix) is not None

    def _find(self, s: str):
        node = self.root
        for c in s:
            node = node.get(c)
            if node is None:
                return None
        return node


if __name__ == "__main__":
    t = PrefixTree()
    t.insert("dog")
    assert t.search("dog") is True
    assert t.search("do") is False
    assert t.startsWith("do") is True
    t.insert("do")
    assert t.search("do") is True
    print("All checks passed")