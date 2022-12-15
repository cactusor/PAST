N, M, X = map(int, input().split())

# 配列Cに値段,配列Aに各アルゴリズムの理解度
C = []
A = []
for _ in range(N):
    ci, *ai = map(int, input().split())
    C.append(ci)
    A.append(ai)

# nで表現される集合に要素iが含まれるかを判定してTrue/Falseを返す関数
def has_bit(n, i):
    return (n & (1<<i) > 0)

# 答えの値.非常に大きい値で初期化して、minで更新する
ans = 10 ** 10

for bit in range(1 << N):
    # 値段,理解度の初期値
    price = 0
    comp = [0] * M
    for i in range(N):
        if has_bit(bit, i):
            price += C[i]
            for j in range(M):
                comp[j] += A[i][j]
    # それぞれのアルゴリズムの理解度がX以上ならば答え(値段)の更新
    flg = True
    for j in range(j):
        if comp[j] < X:
            flg = False
            break
    if flg:
        ans = min(ans, price)

# 答えが10**10ならば答え無しなので-1を出力
if ans == 10 ** 10:
    print(-1)
else:
    print(ans)