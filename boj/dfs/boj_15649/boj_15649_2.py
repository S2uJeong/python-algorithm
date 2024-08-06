"""
중복 없는 순열을 오름차순으로 출력하라.
N : 자연수 , M : 몇 개의 숫자로 조합을 만들어야 하는지 조건
"""
N,M = map(int,input().split())

def solution_print(list):
    for x in list :
        print(x, end = ' ')
    print()

def dfs(depth, visited, tmp_nums):
    if depth >= M :
        solution_print(tmp_nums)
        return
    for i in range(1,N+1):
        if not visited[i]:
            visited[i] = True
            tmp_nums.append(i)
            dfs(depth+1, visited, tmp_nums)
            visited[i] = False
            tmp_nums.pop()

visited = [False] * (N+1)
for i in range(1,N+1):
    visited[i] = True
    dfs(1, visited, [i])
    visited[i] = False
