class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        if n == 0 or m==0:
            return s3 == s1 + s2

        dp = [[0] * (m+1) for _ in range(n+1)]

        def eval(s1, s2, s3, i, j, k):
            if i == n and j == m:
                if k == len(s3):
                    return 1
                else:
                    return -1

            if dp[i][j] == -1:
                return -1
            
            if k >= len(s3):
                return -1
            v = s3[k]

            isPath = -1
            if i+1 <= n and v == s1[i]:
                isPath = eval(s1, s2, s3, i+1, j, k+1)
                dp[i+1][j] = isPath
                if isPath == 1:
                    return isPath

            if j+1<=m and v== s2[j]:
                isPath = eval(s1, s2, s3, i, j+1, k+1)
                dp[i][j+1] = isPath
                if isPath== 1:
                    return isPath

            dp[i][j] = -1
            return -1
        final = eval(s1, s2, s3, 0, 0, 0)

        return final == 1
