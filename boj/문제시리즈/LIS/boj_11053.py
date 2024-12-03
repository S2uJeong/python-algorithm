"""
dp :N^2, binary_search : NlogN
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
nums = list(map(int,input().split()))
def use_dp(): # N^2
    dp = [1] * (N + 1)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
    print(max(dp))


def binary_search(li, target):
    left, right = 0, len(li)-1
    while left <= right:
        mid = (left + right) // 2
        if li[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left
def use_bisect(): # NlogN
    li = []
    for num in nums:
        pos = binary_search(li, num)
        if pos == len(li):
            li.append(num) # target 값 보다 큰게 없다는 뜻이므로 증가하는 수열에 추가
        else:
            li[pos] = num
    print(len(li))

use_bisect()