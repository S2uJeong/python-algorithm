"""
꽃길 복습

화단은 정사각형이고 길이는 6 ~ 10
꽃의 수는 3개
=> 범위가 크지 않아, dfs로 경우의 수 다 구해서 답 구할 수 있음
"""
import sys
input = sys.stdin.readline

result = 1000 # 200 * 5 = 꽃이 차지하는 화단의 최대 비용
dr = [0,0,0,-1,1]
dc = [0,-1,1,0,0]

def is_flower(r,c,visited):
    for k in range(len(dr)):
        kr = r + dr[k]
        kc = c + dc[k]
        if not (0 <= kr < N) or not(0 <= kc < N) or visited[kr][kc]:
            return False
    return True

def check_visited(r,c,visited,flag):
    for k in range(len(dr)):
        kr = r + dr[k]
        kc = c + dc[k]
        visited[kr][kc] = flag
    return visited

def cal_cost(r,c):
    cost = 0
    for k in range(len(dr)):
        kr = r + dr[k]
        kc = c + dc[k]
        cost += matrix[kr][kc]
    return cost
def dfs(flower, visited, cost, r):
    global result
    if flower == 3 :
        result = min(result, cost)
        return

    # 꽃 잎 중심부 이동하며 꽃잎 전개
    for nr in range(r, N-1):
        for nc in range(1,N-1):
            # 꽃잎 전개
            if is_flower(nr,nc,visited):
                # 이 자리에 꽃을 심는다.
                visited = check_visited(nr,nc,visited,1)
                dfs(flower+1,visited, cost + cal_cost(nr,nc), nr)
                visited = check_visited(nr, nc, visited, 0)

N = int(input().rstrip())
matrix = [list(map(int,input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
dfs(0,visited,0,1)
print(result)