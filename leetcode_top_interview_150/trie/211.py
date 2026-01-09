# https://leetcode.com/problems/design-add-and-search-words-data-structure/description/?envType=study-plan-v2&envId=top-interview-150

class WordDictionary:
    def __init__(self):
        self.next = {}
        self.isEnd = False

    def addWord(self, word: str) -> None:
        root = self

        for w in word:
            if not w in root.next:
                node = WordDictionary()
                root.next[w] = node
            
            root = root.next[w]

        root.isEnd = True 
    
    def search2(self, word, root):
        if len(word) == 0 and root.isEnd:
            return True
        n = len(word)
        for i in range(n):
            if word[i] ==  '.':
                for v in root.next.values():
                    if self.search2(word[i+1:], v):
                        return True
                return False
            if word[i] in root.next:
                root = root.next[word[i]]
            else:
                return False
        
        return root.isEnd


    def search(self, word: str) -> bool:
        return self.search2(word, self)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)