import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())

input_list = list(map(int,(input().split())))
dp = input_list[:] # input_list와 같은 내용으로 dp 리스트를 구성하낟.


for i in range(n): # 포인트는 for문의 구성도
    for j in range(i):
        if input_list[j] < input_list[i] : # 오름차순으로 수열을 구해야 하기 때문에
            dp[i] = max(dp[i], dp[j] + input_list[i])
            # max 이유 : j 안을 돌면서, input[i]랑 각 순서의 input[j]랑 비교하면서 input[j]가 작으면 더해지며 dp[i]가 점점 커지는데
            #           바로 전 숫자도 작아서 더해질 수 있을 때, j를 돌며 커진 dp[i] 값이랑 비교함으로써 제일 큰 값으로 유지 가능

result = max(dp)
print(str(result))