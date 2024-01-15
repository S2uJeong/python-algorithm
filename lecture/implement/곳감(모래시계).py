import time
from collections import deque

T = int(input())
in_list = [list(map(int,input().split())) for _ in range(T)]
N = int(input())

def use_list(p_list, N):
    for i in range(N):
        row, way, amt = map(int,input().split())

        if way == 0: # 왼쪽으로
            for j in range(amt):
                p_list[row-1].append(p_list[row-1].pop(0))
        else:
            for j in range(amt):
                p_list[row-1].insert(0,p_list[row-1].pop())
    return p_list

def use_deque(pd_list, N):
    for i in range(N):
        row, way, amt = map(int, input().split())
        if way == 0:  # 왼쪽으로
            for j in range(amt):
                pd_list[row - 1].append(pd_list[row - 1].popleft())
        else:
            for j in range(amt):
                pd_list[row - 1].appendleft(pd_list[row - 1].pop())
    return list(pd_list)

def sum_sand_shape(T, p_list):
# 모래시계 모양으로 합한 수 구하기
    s, e = 0, T
    res = 0
    for i in range(T):
        if i < T//2 :
            for j in range(s,e):
                res += p_list[i][j]
            s += 1
            e -= 1
        else :
            for j in range(s,e):
                res += p_list[i][j]
            s -= 1
            e += 1
    return res

start_time = time.time()
res1 = sum_sand_shape(T,use_list(in_list,N))
end_time = time.time()
print(f'[use_list], result : {res1},  걸린시간 : {end_time - start_time:.5f} sec')


start_time = time.time()
in_deque = deque(in_list)
res2 = sum_sand_shape(T,use_deque(in_deque,N))
end_time = time.time()
print(f'[use_deque], result : {res2},  걸린시간 : {end_time - start_time:.5f} sec')



