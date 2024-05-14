
N, M = map(int,input().split())
data = list(map(int, input().split()))

"""
누적합의 뺄셈 공식 이용 
partSum = prefixSum[j] - prefixSum[i] (i < j)
나머지의 수가 같은 누적합의 조합을 통해 나머지가 0이 되는 부분합의 경우의 수 구할 수 있다. 

"""
r = [0] * M # M으로 나눈 나머지 담는 곳
prefixSum = 0
for i in range(N):
    prefixSum += data[i]
    r[prefixSum % M] += 1

result = r[0] # 나머지가 0이 되는 경우의 수
for i in range(M):
    # nC2 = n(n-1)/2
    result += r[i] * (r[i]-1) // 2

print(result)




"""
O(n) 방법으로 풀어야 함
 - 뒤부터 탐색을 시작하면 그 인덱스까지 더해서 구한 값이 앞에서 쓰여짐.
 - 이를 활용하여 dp list 구상
 - 매 순간 현재 자기 위치에 뒤 idx에 담긴 조합의 합을 더해서 그거랑 더해서 본인 자리 update
"""
def fail(N, M, data) :
    dp = [[] for _ in range(N)]
    cnt = 0
    # dp의 맨 끝은 data의 가장 오른쪽 값으로 초기화
    dp[N-1].append(data[-1])
    if data[-1] % M == 0 :
        cnt +=1
    # dp를 채우며 cnt한다.
    for i in range(N-2, -1, -1): # 끝에서 두번째꺼 부터 그 뒤의 인덱스 기준 dp와 함께 검사한다.
        # 현재 위치 숫자만으로 나누어 떨어질 때
        if data[i] % M == 0 :
            cnt += 1
        # 뒤의 숫자 조합을 더해서 나누어 떨어지는지
        for num in dp[i+1] :
            if (num + data[i]) % M == 0:
                cnt += 1
            dp[i].append(num + data[i])
    return cnt