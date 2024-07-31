"""
1. dfs 없이 풀이
- 수열 : 순서 중요, 중복된 결과는 빼야 한다.
    - 4, 4, 2 인데 길이 1인 수열의 경우의 수 : 2,4
- permutations와 set을 쓰면 문제는 어렵지 않게 풀 수 있는데, 숫자를 문자로 보고 하다보니 출력시 정렬 하는데 조금 어려웠음
  => 이중 리스트여도, 그냥 sort()하면 안에 원소 다 해서 정렬해줌,
2. dfs 사용 (진행중)
"""
import sys
input = sys.stdin.readline
from itertools import permutations
# 입력
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort() # 출력 조건에 맞추기 위해 정렬한다.
# 풀이
result = []
visited = [False] * N
def dfs(arr):
    if len(arr) == M :
        result.append(arr[:])
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            arr.append(nums[i])
            dfs(arr)
            visited[i] = False
            arr.pop()

dfs([])
result = sorted(list(set(map(tuple,result))))
print(result)


for num in set(nums):
    dfs(num)

def use_permu():
    result = []
    # 순열 조합을 result에 담는다.
    for num in permutations(nums, M):
        result.append(num)
    # 출력 조건 : 중복 없음, 정렬
    result = sorted(list(set(result)))
    for li in result:
        for num in li:
            print(num, end = ' ')
        print()
    return
