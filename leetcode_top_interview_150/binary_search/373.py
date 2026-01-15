# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/?envType=study-plan-v2&envId=top-interview-150
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n = len(nums1)
        m = len(nums2)
        if n==0 or m==0:
            return []
        pq = []
        result = []
        visited = {}

        heapq.heappush(pq, (nums1[0] + nums1[0], [0, 0]))
        visited["0-0"] = True

        while len(result) < k:
            min_sum, [i, j] = heapq.heappop(pq)
            result.append([nums1[i], nums2[j]])

            if j+1 < m and (str(i) + '-' + str(j+1) not in visited):
                 heapq.heappush(pq, (nums1[i] + nums2[j+1], [i, j+1]))
                 visited[str(i) + '-' + str(j+1)] = True
            
            
            if i+1 < n and (str(i+1) + '-' + str(j) not in visited):
                 heapq.heappush(pq, (nums1[i+1] + nums2[j], [i+1, j]))
                 visited[str(i+1) + '-' + str(j)] = True


        return result