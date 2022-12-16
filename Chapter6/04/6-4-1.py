INF = float('inf')

N = int(input())
H = list(map(int, input().split()))

# 足場iにたどり着くための最小コスト.サイズNで確保(無限大で初期化).
dp = [INF] * N

# 初期条件
dp[0] = 0

# 2番目以降は1個前の足場と2個前の足場からジャンプできる
for i in range(1, N):
    dp[i] = min(dp[i], dp[i-1] + abs(H[i] - H[i-1]))
    if i > 1:
        dp[i] = min(dp[i], dp[i-2] + abs(H[i] - H[i-2]))

# 最後の足場の最小コストを出力
print(dp[N-1])