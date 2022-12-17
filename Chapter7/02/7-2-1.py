import bisect

N, M = map(int, input().split())
A = list(map(int, input().split()))

# B[k]:子供kが食べた寿司の美味しさ最大値の-1倍
B = [0] * N

for a in A:
    # 寿司を食べる子供を二分探索で探す
    k = bisect.bisect_right(B, -a)
    if k == N:
        print(-1)
    else:
        print(k+1)
        B[k] = -a