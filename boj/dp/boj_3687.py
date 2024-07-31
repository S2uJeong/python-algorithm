"""
숫자는 0으로 시작할 수 없다.
"""
# 가장 작은 수 구하기 위한 dp 생성
dp = [1e19] * 101
# 2~8개 성냥을 가지고 만들 수 있는 최소의 수를 dp에 초기화
dp[2],dp[3],dp[4],dp[5],dp[6],dp[7],dp[8] = 1,7,4,2,6,8,10 # 성냥 갯수가 6일때 0은 맨 앞에 올 수 없으므로 처음 값은 6으로 지정된다.
for num in range(9,101):
    for i in range(2,8):
        if i != 6:
            dp[num] = min(dp[num], dp[num-i]*10 + dp[i])
        else:
            dp[num] = min(dp[num], dp[num-i]*10)

# 가장 큰 수 : 2로 나눈 나머지가 1이면 3개로 7 만들고, 나눈 수 -1 만큼 1로 자릿수 채우기
def make_max_number(n):
    if n % 2 == 1:
        return '7' + '1' * ( (n-3) // 2 )
    else :
        return '1' * (n//2)

T = int(input())
for _ in range(T):
    N = int(input())
    print(dp[N], make_max_number(N))