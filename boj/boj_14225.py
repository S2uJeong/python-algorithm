"""
부분수열의 합
- 문제는 부분 수열인데, 조합문제여서 누적합 방식으로 할 수 없었음
- 그리디 한 밥법, dfs를 활용한 방법이 있음
"""
import sys
input = sys.stdin.readline
N = int(input().rstrip())
nums = list(map(int,input().split()))
check = [False] * 2000000  # 자연수 중 만들 수 없는 가장 작은 숫자 탐색 1 ~ 2_000_000 까지 나올 수 있음
def dfs(idx, sum):
    if idx == N :
        return
    check[sum + nums[idx]] = True
    dfs(idx+1, sum)
    dfs(idx+1, sum + nums[idx])

dfs(0,0)
for num in range(1, len(check)):
    if not check[num]:
        print(num)
        break
def use_sum_array_fail():
    # 누적합은 모든 조합을 고려할 수 없음. 이어지는 수 일때만 가능
    check = [False] * 2000000  # 자연수 중 만들 수 없는 가장 작은 숫자 탐색 1 ~ 2_000_000 까지 나올 수 있음
    # 누적합 배열 만들기
    sums = [0]  # 🟡
    for num in nums:
        sums.append(sums[-1] + num)

    # 누적합으로 조합만들어 check 배열에 표시
    for right in range(len(sums)-1, 0, -1):
        for left in range(0,right):
            new_num = sums[right] - sums[left]
            check[new_num] = True

    # 작은 숫자부터 해당 숫자가 있는지 check 배열 확인
    print(check)
    for num in range(1,len(check)):
        if not check[num]:
            print(num)
            break


