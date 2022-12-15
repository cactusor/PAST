N, M = map(int, input().split())
# 1始まりにするためダミーを入れる.Sは整数に直す
S = [0]
C = [0]
for i in range(M):
    s, c = input().split()
    s_val = 0
    for j in range(N):
        if s[j] == "Y":
            s_val |= 1 << j
    S.append(s_val)
    C.append(int(c))

# 集合としてありうるものの個数.2**Nでも同じ
ALL = 1 << N

# dp[i][n]:セットiまで見て揃った部品の集合がnであるときのコスト最小値
dp = []
INF = 10**100
for i in range(M+1):
    dp.append([INF]*ALL)

# 初期条件
dp[0][0] = 0

# iが小さいところから順に計算
for i in range(1, M+1):
    for j in range(ALL):
        dp[i][j] = min(dp[i][j], dp[i-1][j])
        dp[i][j|S[i]] = min(dp[i][j|S[i]], dp[i-1][j] + C[i])

# 答えは部品が全部揃っている状態の最小コスト
# ただしINFのままなら、部品を揃えることは不可能
ans = dp[M][ALL-1]
if ans == INF:
    ans = -1
print(ans)