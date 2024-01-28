# 이진트리가 아닌 여러 가락으로 뻗는 그래프.
import datetime
n,m = map(int,input().split())

def use_dfs(n,m):
    global res,cnt
    res = [0] * m
    cnt = 0
    DFS(0)
    print(cnt)

def DFS(L):
    global res, cnt
    if L == m :
        for x in res:
            print(x, end =' ')
        print()
        cnt += 1
    else :
        for i in range(1, n + 1):
            res[L] = i
            DFS(L+1)

def use_library(n,m):
    from itertools import product

    nums = list(range(1,n+1))

    pros = list(product(nums, repeat = m))

    for x in pros:
        print(*x)

    print(len(pros))


st = datetime.datetime.now()
use_library(n,m)
end = datetime.datetime.now()
print(f'use_library 걸린시간 : {end-st}')

st = datetime.datetime.now()
use_dfs(n,m)
end = datetime.datetime.now()
print(f'use_DFS 걸린시간 : {end-st}')
