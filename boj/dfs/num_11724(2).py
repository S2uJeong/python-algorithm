# https://www.acmicpc.net/problem/11724
# 기본방법 : 반복문 시작전에 cnt +1 , 이진트리로 탐색 시작, 해당 노드의 값이 안들어간 값이 나올때 마다 cnt +1
# 가지치기 :

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(m)]
status = [1] * n+1 # idx는 노드의 숫자이다. 연결 요소에 쓰였는지 안 쓰였지 상태를 나타낸다.
cnt = 0

def DFS(L,status):
    global cnt
    if sum(status) == 0 :
        return
    else :
        DFS(L+1, )
        cnt += 1

