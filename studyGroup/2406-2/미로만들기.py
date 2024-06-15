import heapq

N = int(input())
# 주어진 입력 값 map 형태로 변환
maps = []
for _ in range(N):
    string = input()
    tmp = []
    for j in range(len(string)):
        tmp.append(int(string[j]))
    maps.append(tmp)

# 최소의 수를 구하는 방식으로 heapq 사용
hq = [(0,0,0)] # cnt, r,c
heapq.heapify(hq)
result = 0

dr = [0,0,-1,1]
dc = [1,-1,0,0]

while True:
    cnt, r, c = heapq.heappop(hq)
    if r == (N-1) and c == (N-1):
        result = cnt
        break

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nc < N and 0 <= nr < N :
            if maps[nr][nc] == 1 : # 흰방이면
                heapq.heappush(hq,(cnt,nr,nc))
            elif maps[nr][nc] == 0 : # 검은방이면
                heapq.heappush(hq, (cnt+1,nr,nc))
            maps[nr][nc] = 2


print(result)

