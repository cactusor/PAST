# キューを使うために読み込み
from collections import deque
# 英小文字一覧を読み込む
from string import ascii_lowercase

Q = int(input())
que = deque()

for q in range(Q):
        # 文字と数字が混ざっているため,いったん文字列で受ける
    values = input().split()
    if values[0] == "1":
        # クエリ1の処理
        c = values[1]
        x = int(values[2])
        que.append([c, x])
    else:
        # クエリ2の処理
        d = int(values[1])
        # 各アルファベットが何文字消されたか.辞書型で管理する
        cnt = {}
        for c in ascii_lowercase:
            cnt[c] = 0
        # 合計d個取り出すか,キューがからになるまで取り出し続ける
        while d > 0 and len(que) > 0:
            c, x = que[0]
            if d >= x:
                # 全部取れるパターン
                d -= x
                cnt[c] += x
                que.popleft()
            else:
                # 途中で切るパターン
                cnt[c] += d
                que[0][1] -= d
                d = 0
        # 答えを計算する
        ans = 0
        for c in ascii_lowercase:
            ans += cnt[c] ** 2
        print(ans)