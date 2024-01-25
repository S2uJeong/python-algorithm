# 부분집합 경우의 수 : 2^n

n = int(input())
ch = [0] *(n+1)  # 쓰는지 안 쓰는지 상태를 보관할 체크변수 (0:사용안한다. 1: 부분집합으로 사용한다.)

def DFS(v):
    if v == n+1 :
        for i, val in enumerate(ch):
            if val == 1:
                print(i, end=' ')
        print()
    else :
        ch[v] = 1
        DFS(v+1)
        ch[v] = 0
        DFS(v+1)

DFS(1)