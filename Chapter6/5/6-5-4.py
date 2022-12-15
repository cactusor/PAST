from collections import defaultdict

N, X = map(int, input().split())

# 偶数番目と奇数番目で半分ずつに振り分けていく
A = []
B = []
for i in range(N):
    w = int(input())
    if i%2 == 0:
        A.append(w)
    else:
        B.append(w)

# nで表現される集合に要素iが含まれるかを判定して
# True/Falseを返す関数
def has_bit(n, i):
    return (n & (1<<i) > 0)

# グループBを全列挙して重さ合計ごとに集計
dic = defaultdict(int)
for n in range(1<<len(B)):
    s = 0
    for i in range(N):
        if has_bit(n, i):
            s += B[i]
    dic[s] += 1

# グループAを全列挙して答えを求める
ans = 0
for n in range(1<<len(A)):
    s = 0
    for i in range(N):
        if has_bit(n, i):
            s += A[i]
    ans += dic[X-s]
print(ans)