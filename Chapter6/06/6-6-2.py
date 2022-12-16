N = int(input())

ans = 0

# Aに1からN-1までの値を順番に代入して試す
for A in range(1, N):
    # Aを固定したときにN>A*Bを満たす正の整数Bの数
    b_count = (N - 1) // A
    ans += b_count

print(ans)