'''
User a*b as pattern to find the graph

graph[a*b] = acb
graph[a*b] = aeb


Also it is important to use BIdirectional BFS

Bidirectional BFS

Bidrectional BFS
'''


from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0
        
        L = len(beginWord)
        patterns = defaultdict(list)

        # Build pattern dictionary
        for word in wordList:
            for i in range(L):
                patterns[word[:i] + "*" + word[i+1:]].append(word)

        queue = deque([(beginWord, 1)])
        visited = set([beginWord])

        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps

            for i in range(L):
                pattern = word[:i] + "*" + word[i+1:]
                for nei in patterns[pattern]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append((nei, steps + 1))
                patterns[pattern] = []  # important optimization

        return 0