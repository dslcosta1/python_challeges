import heapq

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0 or n == 1: return 0
        if n == 2: return max(0, prices[1] - prices[0])

        dp = [0] * (n+2) 
        pq = []
        heapq.heappush(pq, (-prices[-1], n-1))

        for i in range(n-2, -1, -1):
            biggest, j  = heapq.heappop(pq)
            visited = [(biggest, j)]
    
            while -biggest > prices[i]:
                dp[i] = max(dp[i], prices[j] - prices[i] + dp[j+2])

                if pq:
                    biggest, j  = heapq.heappop(pq)
                    visited.append((biggest, j))
                else:
                    break
            
            for v in visited:
                heapq.heappush(pq, v)

            dp[i] = max(dp[i], dp[i+1])
            heapq.heappush(pq, (-prices[i], i))

        return dp[0]
