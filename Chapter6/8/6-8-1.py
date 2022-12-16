N = int(input())

# X[d]: d日目から実行可能になるタスクのポイントを集めた配列
X = []
for i in range(N):
    X.append([])
for i in range(N):
    a, b = map(int, input().split())
    X[a-1].append(b)

cnt = [0]*101
ans = 0
for d in range(N):
    # d日目から実行可能になるタスクをcntに追加する
    for b in X[d]:
        cnt[b] += 1
    
    # cnt[b] > 0 である最大のbを探して加算する
    for b in range(100, 0, -1):
        if cnt[b] > 0:
            ans += b
            cnt[b] -= 1
            break
    print(ans)