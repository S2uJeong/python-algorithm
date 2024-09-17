"""
deque : 오름차순으로 들어오는 수를 받아, 오름차순으로 조합을 출력하기 위해 사용한다.
범위
- 숫자는 1 ~ 49 , K ( 7 ~ 12 )

DFS (nums: 입력된 숫자, start: 시작 숫자 idx, combi : 현재 만든 조합 )
    - combi.length == K 면 return
"""
import sys
input = sys.stdin.readline

def dfs(nums, start, combi):
    if len(combi) == 6:
        print(*combi)
        return

    for i in range(start, len(nums)):
        combi.append(nums[i])
        dfs(nums, i+1, combi) # 다음 숫자는 현재 숫자 이후의 숫자들만 고려
        combi.pop() # 백트래킹 : 선택을 취소하고 다른 경로 탐색

while True:
    nums = list(map(int,input().split()))
    if len(nums) <= 1: break

    dfs(nums[1:], 0, [])
    print()

