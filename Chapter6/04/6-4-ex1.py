INF = float('inf')

N, K = map(int, input().split())
H = list(map(int, input().split()))

# 足場iにたどり着くための最小コスト.サイズNで確保(無限大で初期化).
dp = [INF] * N

# 初期条件
dp[0] = 0

for i in range(1, N):
    # 1～K個前の足場からジャンプした場合のコストを計算する
    for j in range(1, K+1):
        # j個前の足場の確認
        if j <= i:
            dp[i] = min(dp[i], dp[i-j] + abs(H[i] - H[i-j]))

# 最後の足場の最小コストを出力
print(dp[N-1])