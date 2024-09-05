import sys
input = sys.stdin.readline

def find_next_greater_elements(nums):
    stack = []
    answer = [-1] * N
    for i in range(N):
        while stack and nums[stack[-1]] < nums[i]:
            answer[stack.pop()] = nums[i]
        stack.append(i)
    return answer

N = int(input().rstrip())
nums = list(map(int,input().split()))
answer = find_next_greater_elements(nums)

for a in answer:
    print(a, end= ' ')