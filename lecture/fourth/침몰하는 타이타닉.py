from collections import deque
N, L = map(int,input().split())
w_list = list(map(int,input().split()))
res = 0
w_list.sort(reverse=True)
w_que = deque(w_list)
while w_que:
    if w_que[0] + w_que[-1] > L :
        w_que.popleft()
        res += 1
    else :
        w_que.popleft()
        if w_que: # 이 구문이 있어야 "pop from an empty deque" 오류가 발생하지 않음.
            w_que.pop()
        res += 1
print(res)
