def solution(m, n, puddles):
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1

    for [x,y] in puddles: 
        dp[y-1][x-1] = -1

    for i in range(1, m):
        if dp[0][i] == -1: 
            continue
        dp[0][i] = max(0, dp[0][i-1])

    for i in range(1, n):
        if dp[i][0] == -1: 
            continue
        dp[i][0] = max(0, dp[i-1][0])

    for r in range(1, n):
        for c in range(1, m):
            if dp[r][c] == -1: 
                continue
            if dp[r-1][c] in (-1, 0) and dp[r][c-1] in (-1, 0): 
                dp[r][c] = 0 
            else: dp[r][c] = max(dp[r-1][c], 0) + max(dp[r][c-1], 0)

    return dp[-1][-1]%1000000007