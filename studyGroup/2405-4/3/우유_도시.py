"""
bfs로 보이는 문제에서 최소/최대 방법을 찾는 문제 => DP
milk 조건을 각 케이스별로 달리해서 비교하는게 어려웠음
    3차원 배열로 해당 자리에서 우유를 먹는다 안 먹는다로 구분해서 풀면 되는 문제

- Ture/False로 우유 cnt를 늘린 것과, if - else를 한줄로 하여 변수를 업데이트 한 방법이 좋음
"""
import sys
input = sys.stdin.readline

N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0, -1] for _ in range(N+1)] for _ in range(N+1)]  # [0,-1] : 현재 칸 까지의 count, milk

for i in range(1, N+1):
    for j in range(1, N+1):
        left, up = dp[i][j-1], dp[i-1][j]
        is_continue_left = maps[i-1][j-1] == (left[1]+1) % 3 # for문이 dp 기준으로 돌고 있어서 maps index에는 각 -1 한 값이 현재위치임
        is_continue_up = maps[i-1][j-1] == (up[1]+1) % 3

        new_left_score = left[0] + is_continue_left
        new_up_score = up[0] + is_continue_up

        if new_up_score > new_left_score:
            dp[i][j][0] = new_up_score
            dp[i][j][1] = maps[i-1][j-1] if is_continue_up else up[1]
        else :
            dp[i][j][0] = new_left_score
            dp[i][j][1] = maps[i-1][j-1] if is_continue_left else left[1]


print(dp[N][N][0])