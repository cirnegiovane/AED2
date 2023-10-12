def intPart(valor):
    dp = [[-1 for x in range(valor+1)] for y in range(valor+1)]

    for i in range(valor+1):
        dp[0][i] = 0
        dp[i][0] = 1

    for i in range(1, valor+1):
        for j in range(1, valor+1):
            if(j >= i):
                dp[i][j] = dp[i-1][j] + dp[i][j-i]
            else:
                dp[i][j] = dp[i-1][j]

    return dp[valor][valor]


print(intPart(5))