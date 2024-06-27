"""
연속하는 증가 수열의 최대 길이 구하기 = DP
dp에 사용되는 memo 리스트는 현재 위치까지 밟을 수 있는 징검다리 개수를 뜻한다.
"""

import sys
input = sys.stdin.readline

N = int(input().rstrip())
nums = list(map(int,input().split()))
memo = [1] * N  # 자기 자신 칸만 밟아도 1씩은 됨

for i in range(1,N):
    for j in range(i):
        if nums[j] < nums[i]:
            memo[i] = max(memo[i], memo[j]+1)

print(max(memo))