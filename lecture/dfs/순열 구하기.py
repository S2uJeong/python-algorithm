n,m = map(int,input().split())
def use_library(n,m):
    from itertools import permutations
    pms = list(permutations(list(range(1,n+1)),m))
    pms.sort()
    # 출력 시작
    for x in pms:
        print(*x)
    print(len(pms))

res = [0] * m
ch = [0] * (n+1)
cnt = 0
def use_dfs(n,m):
    dfs(0)
    print(cnt)
# L(노드) : m, 자릿수를 뜻한다.
# 가지(간선) : 1 ~ n 어떤 숫자를 조합할지
def dfs(L):
    global res,ch,cnt
    if L == m :
        print(*res)
        cnt+=1
    else :
        for i in range(1,n+1):
            if ch[i] == 0:
                res[L] = i
                ch[i] = 1
                dfs(L+1)
                # dfs 호출 아래에 있는 명령은 돌아와서 실행되는 부분임을 상기.
                ch[i]=0

from datetime import datetime
s = datetime.now()
use_library(n, m)
#use_dfs(n, m)
e = datetime.now()
print(f'걸린시간 : {(s-e).seconds}')
