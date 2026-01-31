
class Solution:
    results = []
    def perm(self, nums, piece, val):

        if len(nums) <= len(val):
            self.results.append(val)
            return 
        
        n = len(piece)
        copy_piece = piece[:]
        for i in range(n):
            
            v = copy_piece.pop(i)
            self.perm(nums, copy_piece, val + [v])


            copy_piece = piece[:]
        
        return

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.results = []
        self.perm(nums, nums, [])

        return self.results