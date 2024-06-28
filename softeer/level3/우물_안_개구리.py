import sys
input = sys.stdin.readline

N, M = map(int, input().split())
weights = list(map(int,input().split()))
graph = [[] for _ in range(N+1)] # input으로 주어지는 회원 번호가 1 ~ N으로 주어지므로 맞춰준다.

for _ in range(M):
    node1, node2 =  map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

result = 0
for idx, w in enumerate(weights):
    flag = True # 난 최고얌!
    for next_id in graph[idx+1]: # list의 idx와 input의 회원번호와 맞춰주기 위해 idx + 1
        if weights[next_id-1] >= w :
            flag = False
    if flag :
        result += 1

print(result)