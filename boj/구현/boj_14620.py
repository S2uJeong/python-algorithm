"""
신경써야 하는 것
1. 꽃은 씨앗이 뿌린 지점에서 상하좌우로 뻗어 총 5칸을 차지
2. 꽃끼리 부딪히면 안됨
3. 꽃이 화단 바깥으로 나가면 안됨
=> 위 조건을 만족하며 화단 대여료가 가장 적을 곳에 씨앗을 3개 심고 그 대여 최소 비용을 출력한다.
"""
from itertools import combinations

N = int(input()) # 6 ~ 10
maps = [list(map(int,input().split())) for _ in range(N)]
dr = [1,-1,0,0]
dc = [0,0,-1,1]

def calc(combi):
    visited = []
    total = 0
    global result

    for r,c in combi:
        if (r,c) not in visited:
            visited.append((r,c))
            total += maps[r][c]
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if (nr,nc) not in visited:
                    visited.append((nr,nc))
                    total += maps[nr][nc]
                else:
                    return
        else:
            return
    result = min(result, total)

result = 1e9

tmp = [(r,c) for r in range(1,N-1) for c in range(1,N-1)]
for combi in combinations(tmp, 3):
    calc(combi)

print(result)
