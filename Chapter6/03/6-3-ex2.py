from collections import deque

K = int(input())

# キューを用意して、1桁台のルンルン数を入れる
Q = deque()
for i in range(1, 10):
    Q.append(i)

# ルンルン数の小さい方からの番号
lunlun = 0

while len(Q) > 0:
    n = Q.popleft()
    lunlun += 1
    # K番目のルンルン数であれば終了
    if lunlun == K:
        break
    unit_digit = n % 10
    # 1の位が0より大きかったら10倍して(1の位)-1を足した数がルンルン数
    if unit_digit > 0:
        Q.append(10 * n + unit_digit - 1)
    # 10倍して(1の位)を足した数がルンルン数
    Q.append(10 * n + unit_digit)
    # 1の位が9より小さかったら10倍して(1の位)+1を足した数がルンルン数
    if unit_digit < 9:
        Q.append(10 * n + unit_digit + 1)

# K番目のルンルン数を出力
print(n)