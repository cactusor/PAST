from collections import deque

N, X, Y = map(int, input().split())

# そのマスが通れるかどうかの二次元配列.
# 目標に回り込んで行けるグリッド(-201~0~201:403マス)を確保.
Grid = [[True] * 403 for _ in range(403)]
# 中央
mid_x, mid_y = 403//2, 403//2
# スタート地点
sx, sy = mid_x, mid_y

# 障害物の設定.
for _ in range(N):
    xi, yi = map(int, input().split())
    # 障害物のマスは通れないのでFalseにする.
    Grid[xi + mid_x][yi + mid_y] = False

# スタート地点からの最小移動回数を管理する2次元配列.
# -1であれば未訪問であることを表す.
dist = [[-1] * 403 for _ in range(403)]

# キューを用意して、始点を入れる
Q = deque()
Q.append([sx, sy])
dist[sx][sy] = 0

# キューを取り出しながら探索する
while len(Q) > 0:
    i, j = Q.popleft()
    # 6つの隣マスを確認する
    for i2, j2 in [[i+1, j+1], [i, j+1], [i-1, j+1], [i+1, j], [i-1, j], [i, j-1]]:
        # もし範囲内でなければ無視する
        if not (0 <= i2 < 403 and 0 <= j2 < 403):
            continue
        # もし壁マスであれば無視する
        if not Grid[i][j]:
            continue
        # もし未訪問(dist[i2][j2]が-1)であれば、距離を更新してキューに入れる
        if dist[i2][j2] == -1:
            dist[i2][j2] = dist[i][j] + 1
            Q.append([i2, j2])

# 始点から終点までの最小移動回数を出力
print(dist[X + mid_x][Y + mid_y])