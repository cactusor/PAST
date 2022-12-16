# ∞を表す定数として,非常に大きい数を用意しておく(10**18)
INF = 1_000_000_000_000_000_000

N, M = map(int, input().split())

# 全ての頂点の組についての最短距離を保存する2次元配列distを作る
dist = []
# 最初は辺が1本も張られていないため、∞の辺が張られているとして
# N × N 個のINFで埋めておく
for i in range(N):
    dist.append([])
    for j in range(N):
        dist[i].append(INF)

# グラフの辺を受け取り,distに直接書き込む
for _ in range(M):
    u, v, c = map(int, input().split())
    dist[u][v] = c

# iからiへの同じ頂点同士の距離は0としておく
for i in range(N):
    dist[i][i] = 0

# ワーシャル-フロイド法
for k in range(N):
    for x in range(N):
        for y in range(N):
            dist[x][y] = min(dist[x][y], dist[x][k] + dist[k][y])

# 全ての頂点の組について最短距離を合計する
ans = 0
for i in range(N):
    for j in range(N):
        ans += dist[i][j]

print(ans)