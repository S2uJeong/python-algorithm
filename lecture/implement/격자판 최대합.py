def get_sum_of_diagonal(idx_i_str,N,table):
    sum = 0
    if idx_i_str == 0 :
        for i in range(N):
            sum += table[i][i]
    if idx_i_str == N-1 :
        for i in range(N):
            sum += table[i][N-1-i]
    return sum

N = int(input())
table = [list(map(int,input().split())) for _ in range(N)]
max = -1e9

for i in range(N):
    sum_row = sum_col = 0
    for j in range(N):
        sum_row += table[i][j]
        sum_col += table[j][i]
        if sum_row > max :
            max = sum_row
        if sum_col > max :
            max = sum_col
# 대각선 계산
sum1 = sum2 = 0
if i == 0 and j == 0:
    sum1 = get_sum_of_diagonal(i,N,table)
    if sum1 > max :
        max = sum1
if i == N-1 and j == 0 :
    sum2 = get_sum_of_diagonal(i,N,table)
    if sum2 > max :
        max = sum2

print(max)



