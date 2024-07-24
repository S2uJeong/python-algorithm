"""
집의 양쪽 색과 다른 색을 칠해야 하며, (집,색상) 별로 가격이 정해져 있다. 집을 다 칠하기 위한 색 비용을 최소화 하라.
집의 수는 2 ~ 1000

- dfs : 시간 초과
- dp : 통과
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
costs = [list(map(int,input().split())) for _ in range(N)]
result = INF = int(1000 * 1000)
for start_color in range(3):
    dp = [[INF] * 3 for _ in range(N)]
    dp[0][start_color] = costs[0][start_color]
    for i in range(1,N):
        dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1])

    for k in range(3):
        if start_color != k:
            result = min(result, dp[-1][k])

print(result)



def use_dfs(): # 시간초과
    N = int(input().rstrip())
    costs = [list(map(int, input().split())) for _ in range(N)]
    result = int(1000 * 1000)
    def dfs(n, start_color, color, crt_cost): # start_color = [0:빨강, 1:초록, 2:파랑]
        global result
        # 종료조건
        if n >= N :
            result = min(result, crt_cost)
            return
        # 마지막 노드에선 돌아오는 노드의 색상을 고려해야 함
        if n == N - 1:
            if color == start_color:
                return

        for next_color in range(3):
            if color != next_color:
                dfs(n+1, start_color, next_color, crt_cost + costs[n][color])

    for start_color in range(3):
        dfs(0, start_color, start_color, 0)

    print(result)
