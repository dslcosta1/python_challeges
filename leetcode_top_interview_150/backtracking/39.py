

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if target <= 0:
            return []

        n = len(candidates)
        results = []
        for i in range(n):
            element = candidates[i]

            permutations = self.combinationSum(candidates[i:], target - element)
            if permutations != None:
                if len(permutations) == 0:
                    if element == target:
                        results.append([element]) 
                for permutation in permutations:
                    if permutation != None:
                        permutation.append(element)
                        if sum(permutation) == target:
                            results.append(permutation)
            
        return results