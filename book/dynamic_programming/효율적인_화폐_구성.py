# 입력받기
n,m = map(int,input().split())

arr = []
# 단위 값은 엔터를 기준으로 차례대로 들어온다.
for i in range(n):
    arr.append(int(input()))

# 1. 목표금액(m)별로 값을 저장할 수 있는 memo 배열을 만들고, 초기화는 10001로 한다.
memo = [10001] * (m + 1)

memo[0] = 0  # 목표 금액이 0일 땐, 화폐 0개로 구성 가능 / 목표금액 - 화폐단위이 0이 될 시 memo[목표금액] 값을 0+1 로 만들어 줄 조건
for i in range(n): # 화폐 단위 개수 만큼
    for j in range(arr[i], m + 1): # 화폐 단위 숫자부터, 목표금액까지
        if memo[j-arr[i]] != 10001:
            memo[j] = min(memo[j], memo[j - arr[i]] + 1)

if memo[m] == 10001:
    print(-1)
else:
    print(memo[m])