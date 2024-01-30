s,e = map(int,input().split())

# 최소 횟수를 충족하는 요건
# 1. 5번 점프 활용하기 (e-s >=4 일 때만)
cnt = 0
def solution(s,e):
    global cnt
    while e != s:
        if e-s >= 4:
            s += 5  # 앞으로 5
        elif e > s :
            s += 1 # 앞으로 1
        else :
            s -= 1
        cnt += 1
    print(cnt)

def use_bfs(s,e):
    from collections import deque
    # 문제에서 좌표는 1 ~ 10000 범위라고 주어짐.
    max = 10000
    # dis 리스트 : idx - 위치, val - 몇 번만에 간건지
    dis = list(range(max+1))
    # ch 리스트 : 이전에 방문한 적 있는 위치인지
    ch = [0] * (max+1)
    dQ = deque()
    # 시작 노드
    ch[s] = 1
    dis[s] = 0
    dQ.append(s)

    while dQ :
        now = dQ.popleft()
        if now == e :
            break
        for next in (now-1, now+1, now+5):
            # 음수로 가는것 방지
            if 0 < next :
                if ch[next] == 0:
                    dQ.append(next)
                    ch[next] = 1
                    dis[next] = dis[now] + 1

    print(dis[e])


import datetime
st = datetime.datetime.now()
#use_bfs(s,e)
solution(s,e)
end = datetime.datetime.now()
print(f'걸린시간 : {end-st}')

# 3 4356 으로 입력시,
# use_bfs(s,e) - 0.005246
# solution(s,e) - 0.000362  : 성능,메모리 둘다 win!!!