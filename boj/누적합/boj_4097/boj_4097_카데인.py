"""
테스트케이스가 몇 개인진 모름
수익을 기록한 날짜는 1~250,000
O(n)으로 해결해본다.

1. 최대 부분 배열 합 : 카데인 알고리즘 (더 성능 좋음)
2. 누적합 방법
"""
import sys
input = sys.stdin.readline

# 🔴최대 부분 배열 합
def max_subarray_sum(arr):
    max_ending_here = result = arr[0]
    for num in arr[1:]:
        max_ending_here = max(num, max_ending_here + num)
        result = max(result, max_ending_here)
    return result

# 🔴누적합 사용
def max_subarray_sum_prefix(arr):
    n = len(arr)
    if n == 0:
        return 0

    prefix_sum = [0] * (n+1)
    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + arr[i]

    max_sum = -(1e9)
    min_prefix_sum = 0

    for i in range(1,n+1):
        max_sum = max(max_sum, prefix_sum[i] - min_prefix_sum)
        min_prefix_sum = min(min_prefix_sum, prefix_sum[i])
    return max_sum

while True :
    N = int(input())
    if N == 0 :
        break
    benefits = [int(input()) for _ in range(N)]
    result = max_subarray_sum_prefix(benefits)

    # 출력
    print(result)