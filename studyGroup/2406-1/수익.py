"""
테스트케이스가 몇 개인진 모름
수익을 기록한 날짜는 1~250,000
O(n)으로 해결해본다.

첫번째 시도. 누적합
1. 수익을 적어 논 기록을 놀며 각 자리에 누적합을 메모리에 따로 저장 (for문 1번)
2. 이중 for문을 i는 1 ~ n j는 0 ~ i 로 돌며 data[i] - data[j] 해서 max 값을 업데이트
3. 공식을 구할 수 없음. 실패

두번째 시도. 최대 부분 배열 합 : 카데인 알고리즘
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

while True :
    N = int(input())
    if N == 0 :
        break
    benefits = [int(input()) for _ in range(N)]
    result = max_subarray_sum(benefits)

    # 출력
    print(result)
