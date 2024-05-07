from collections import deque
N = int(input())
data = list((map(int, input().split())))
S = int(input())

def count_visited(visited):
    cnt = 0
    for bool in visited:
        if bool == True:
            cnt += 1
    return cnt

dQ = deque() #(data에서 시작 인덱스, cnt)
dQ.append((S-1, 1))
visited = [False] * N
visited[S-1] = True
def bfs() :
    while dQ:
        now, cnt = dQ.popleft()
        # 이미 방문한(dQ에 돌을 넣은) 횟수가 N개 이상이면 다 방문한거니 멈춰라.
        if cnt == N :
            return cnt
        nl = now - data[now]
        nr = now + data[now]
        if 0 <= nl < N and not visited[nl] :
            dQ.append([nl, cnt + 1])
            visited[nl] = True
        if 0 <= nr < N and not visited[nr]:
            dQ.append([nr, cnt + 1])
            visited[nr] = True

    # dQ가 빌 때 까지, cnt가 N이 안 되었으면 그 횟수만큼만 반환
    result = count_visited(visited)
    return result

print(bfs())