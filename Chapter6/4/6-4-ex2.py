N, W = map(int, input().split())
# 1始まりにするために先頭にダミーを入れる
ws = [0]
vs = [0]
for i in range(N):
    w, v = map(int, input().split())
    ws.append(w)
    vs.append(v)

# 価値の総和は価値の最大値10**3と品数の最大値10**2の積
V = 10**5

# weight[i][v]:品物iまで見て価値の総和vであるときの重さの合計
# 非常に大きい値で初期化しておく
weight = [[10**18] * (V+1) for _ in range(N+1)]

# 初期条件
weight[0][0] = 0

# iが小さい順に求めていく
for i in range(1, N+1):
    for v in range(V+1):
        # 品物iを使わない場合
        weight[i][v] = min(weight[i][v], weight[i-1][v])
        # 品物iを使う場合
        if v-vs[i] >= 0:
            weight[i][v] = min(weight[i][v], weight[i-1][v-vs[i]] + ws[i])

# weight[N][0], ..., weight[N][V]の中で重量がW以下のインデックスviが答え
ans = -1
for vi in range(V+1):
    if weight[i][vi] <= W:
        ans = vi
print(ans)

# PyPyで提出