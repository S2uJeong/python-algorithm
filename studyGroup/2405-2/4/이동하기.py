"""
전진할 때 마다 그 전 수량(dp) 현재 값 합해서 memo해 두고, 그 중에서 최고 값 나온것을 반환 = 오른쪽 방향으로만 전진해서 가능한 로직
point - 이동 후 위치에서 이동 전 경우의 수 중 가장 큰 dp값을 가진 것을 선택.
"""
N, M = map(int, input().split())
data = [list(map(int,input().split())) for _ in range(N)]
dp = [[0] * (M+1) for _ in range(N+1)] # (0,0)에서 그 이전 위치의 값이 0일 수 있게 길이를 늘려줌

for i in range(1,N+1): # 시작은 맨 왼쪽 위 보다 한 칸 띄어서 해야한다. (이전 이동 중 큰걸 가져오는 dp이기 때문)
    for j in range(1,M+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + data[i-1][j-1] # data는 idx 안 늘려줌에 유의

print(dp[N][M])