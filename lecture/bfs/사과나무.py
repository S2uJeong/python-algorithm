from collections import deque
import datetime
stime = datetime.datetime.now()

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]

dQ = deque([])
dQ.append((N//2, N//2, 0)) # 한 행에서 start/end 하는 열의 위치, 현재 행의 위치
res = 0
while dQ:
    start,end,row = dQ.popleft()
    # 1. 문제 조건에 맞는지 확인
    if row < N:
        # 2. queue에 들어 있는 위치를 토대로 graph에서 사과나무 갯수를 찾아 res에 더해준다.
        for j in range(start, end+1):
            res += graph[row][j]
        # 3. 다음 위치를 넣어준다.
        #   * 행의 위치에 따라 시작점과 끝점의 규칙이 달라진다 (다이아몬드 모양)
        if row+1 <= N//2 :
            dQ.append( (start-1, end+1, row+1) )
        else :
            dQ.append( (start+1, end-1, row+1) )
etime = datetime.datetime.now()
print(res)
print(f'걸린시간 : {etime - stime}')