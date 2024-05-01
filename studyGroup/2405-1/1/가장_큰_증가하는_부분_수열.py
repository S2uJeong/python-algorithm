"""
- 진행방향이 오른쪽으로 지정되었고
- 증가하는 수열이므로 왼쪽에 있는 메모(증가하는 방향으로 더해진 수)는 현재 포인터 값보다 작기만 하면
현재 대상의 더해질 대상이 됨.
- 현 포인터에서 왼쪽으로 대상되는 것들 찾아보고 최대값 인걸로 골라 현 포인터 값과 더해 메모에 업데이트 한다.
- memo값 중에 제일 큰 값을 max()함수로 찾아 반환
"""
N = int(input())
data = list(map(int, input().split()))
dp = [1] * N
dp[0] = data[0]
for i in range(N):
    for j in range(i):
        if data[j] < data[i]:
            dp[i] = max(dp[i], dp[j]+data[i])
        else :
            dp[i] = max(dp[i], data[i])

print(max(dp))