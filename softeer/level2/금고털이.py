"""
무게당 가격이 높은 순으로 정렬하여 답을 구한다.
"""
import sys
input = sys.stdin.readline

W, N = map(int, input().split())
jewels = [list(map(int,input().split())) for _ in range(N)]
jewels.sort(key = lambda x : -x[1])

result = 0
for stock, price in jewels:
    if W - stock < 0 :
        result += (W * price)
        break
    else :
        W -= stock
        result += (stock * price)

print(result)


