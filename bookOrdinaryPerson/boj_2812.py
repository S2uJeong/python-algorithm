"""
인덱스를 순회하며 왼쪽 값이 현재 값보다 크면 냅두고, 작으면 바꾼다.
만약 N-K개 보다 많은 수가 이어지면, 슬라이스를 통해 숫자를 반환한다.
"""
N, K = map(int, input().split())
nums = list(input())
stack = []

k = K
for i in range(N):
    while (k > 0 and stack and stack[-1] < nums[i]):
        stack.pop()
        k -= 1
    stack.append(nums[i])

print(''.join(stack[:N - K]))
