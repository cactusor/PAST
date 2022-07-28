INF = float('inf')

N, L = map(int, input().split())
X = list(map(int, input().split()))
T1, T2, T3 = map(int, input().split())

# ハードルがある座標においてTrueとなるような配列H
H = [False] * (L+1)
for x in X:
    H[x] = True

# dp[i]:座標iで行動を終了するまでの最小所要時間
# 非常に大きな値で初期化しておき、minを用いて更新する
dp = [INF] * (L+1)

# 初期条件
dp[0] = 0

# 順番に求めていく
for i in range(1, L+1):
    # 行動1
    dp[i] = min(dp[i], dp[i-1] + T1)
    # 行動2
    if i >= 2:
        dp[i] = min(dp[i], dp[i-2] + T1 + T2)
    # 行動3
    if i >= 4:
        dp[i] = min(dp[i], dp[i-4] + T1 + 3 * T2)
    # ハードルがあれば加算
    if H[i]:
        dp[i] += T3

# ジャンプ中にゴールした場合を計算する(座標(L-3)～(L-1))
for i in [L-3, L-2, L-1]:
    if i >= 0:
        dp[L] = min(dp[L], dp[i] + T1 // 2 + T2 * (2 * (L-i) - 1) // 2)

# 座標Lの値を出力
print(dp[L])