# https://leetcode.com/problems/minimum-genetic-mutation/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def isMutation(self, a, b):
        n = len(a)
        diff = 0
        for i in range(n):
            if a[i] != b[i]: diff += 1
        
        return diff == 1

    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if not endGene in bank: return -1
        if self.isMutation(startGene, endGene): return 1
        old_stack = []
        new_stack = []
        visited = {}
        path_size = 1
        old_stack.append(startGene)

        while len(old_stack) > 0:
            #print(old_stack)
            gene = old_stack.pop()
            visited[gene] = True
            for b in bank:
                #print(b)
                if not b in visited and self.isMutation(gene, b):
                    if b == endGene: return path_size

                    new_stack.append(b)
                        
                    
            if len(old_stack) == 0:
                old_stack = new_stack[:]
                new_stack = []
                path_size += 1
        
        return -1