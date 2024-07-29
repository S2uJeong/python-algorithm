"""
bfs : 해당 노드를 방문하는게 최소 거리임을 보장함.
dQ를 이용해서, 1번 부터 시작해서 갈 수 있는 곳을 다 넣으며 확인하고, 100이 나오면 반환한다.
"""
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
# 특별 경로 딕셔너리
swap_list = dict() # key : 출발지 , value : 도착지
for _ in range(N+M):
    fr, to = map(int,input().split())
    swap_list[fr] = to
def bfs(start_num, count):
    visited = [False] * 101 # idx로 숫자를 표현
    dQ = deque([(start_num, count)])
    visited[start_num] = True
    while dQ:
        crt_num, count = dQ.popleft()
        # 만약 현재 숫자가 100이면, return 한다.
        if crt_num == 100:
            return count
        # 그냥 경로일 때는 주사위 값을 더해주고, count를 더해서 넣어준다.
        for num in range(1,7): # 주사위
            next_num = crt_num + num
            if next_num <= 100 and not visited[next_num] :
                # 주사위의 위치가 이벤트위치면, 이벤트 시행 이후의 값으로 넣는다.
                for key in swap_list:
                    if key == next_num:
                        next_num = swap_list[next_num]
                dQ.append((next_num, count + 1))
                visited[next_num] = True

# 1부터 시작하는 bfs
print(bfs(1,0))








