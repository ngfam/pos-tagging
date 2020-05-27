class TrieNode:
    def __init__(self):
        self.children = [None] * 30
        self.tagCount = dict()
        #taglist shall be tuple (tagname, probability)
        self.tagList = [] 


class Trie:
    def getNode(self):
        return TrieNode()

    def __init__(self):
        self.root = self.getNode()
    
    def _charToIndex(self, ch):
        if ch == '<':
            return 26
        if ch == '>':
            return 27
        if ch == '/':
            return 28
        if ord(ch) in range(97, 123):
            return ord(ch) - ord('a')
        return 29

    def insert(self, key, tag):
        curNode = self.root
        for ch in key:
            id = self._charToIndex(ch)
            if curNode.children[id] is None:
                curNode.children[id] = self.getNode()
            curNode = curNode.children[id]
        if tag in curNode.tagCount:
            curNode.tagCount[tag] += 1
        else:
            curNode.tagCount[tag] = 1

    def searchTag(self, key):
        curNode = self.root
        for ch in key:
            id = self._charToIndex(ch)
            if curNode.children[id] is None:
                return ("<unk>", dict())
            curNode = curNode.children[id]
        return (key, curNode.tagList)

    def dfs(self, node):
        if len(node.tagCount) != 0:
            tot = 0
            for key in node.tagCount:
                tot += node.tagCount[key]

            for key in node.tagCount:
                node.tagList.append((key, node.tagCount[key] / tot))
        
        for i in range(30):
            if node.children[i] is not None:
                self.dfs(node.children[i])
    
    def build(self):
        self.dfs(self.root)
