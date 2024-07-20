"""
누적합과 이중포인터를 이용하여 푼다.

M보다 작은지, 큰지, 같은지를 조건으로 포인터를 조절하고 매 순간 해당 idx까지의 합을 전달하여 계산을 줄인다.

"""
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
nums = list(map(int,input().split()))

# 누적합 만들기
stack_nums = [0] # 앞에 0은 투포인터에서 쿠션 역할을 함
sum = 0
for num in nums:
    sum += num
    stack_nums.append(sum)

# 투 포인터로 조절하며 경우의 수 구하기
answer = 0
left, right = 0, 0

while right <= N :
    tmp_sum = stack_nums[right] - stack_nums[left]
    if tmp_sum == M :
        answer += 1
        left += 1
        right += 1
    elif tmp_sum < M :
        right += 1
    else :
        left += 1

    if left == right:
        right += 1

print(answer)