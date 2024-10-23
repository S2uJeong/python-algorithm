"""
가장 긴 증가하는 부분 수열 2
dp로는 시간 초과
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
nums = list(map(int,input().split()))

def binary_search(li, target):
    left, right = 0, len(li)-1
    while left <= right:
        mid = (left + right) // 2
        if target > li[mid]:
            left = mid + 1
        else :
            right = mid - 1
    return left

li = []
for num in nums:
    pos = binary_search(li, num)
    if pos >= len(li):
        li.append(num)
    else:
        li[pos] = num


print(len(li))

