N = int(input())
A =[]
for i in range(N):
    a = list(map(int, input().split()))
    A.append(a)
ALL = 1<<N

# dp[n][i]:訪れた年の集合がnで、最後にいる都市がiであるときのコスト最小値
dp = []
for n in range(ALL):
    dp.append([10**100]*N)

# 初期条件.最初にいるときの始点はnには含めない
dp[0][0] = 0

# nで表現される集合に要素iが含まれるかを判定してTrue/Falseを返す関数
def has_bit(n, i):
    return (n & (1<<i) > 0)

for n in range(ALL):
    for i in range(N):
        # iからjに移動する遷移を試す
        for j in range(N):
            if has_bit(n, j) or i == j:
                continue
            dp[n|(1<<j)][j] = min(dp[n|(1<<j)][j], dp[n][i] + A[i][j])
print(dp[ALL-1][0])