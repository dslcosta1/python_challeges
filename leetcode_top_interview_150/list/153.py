class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        n = len(ratings)
        leftToRight = [1] * n
        rightToLeft = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                leftToRight[i] = leftToRight[i-1] + 1

            if ratings[n-1-i] > ratings[n-i]:
                rightToLeft[n-1-i] = rightToLeft[n-i] + 1
        
        max_candys = []
        for i in range(n):
            max_candys.append(max(leftToRight[i], rightToLeft[i]))
        return sum(max_candys)