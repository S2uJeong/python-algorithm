"""
K번째 수
- 값의 범위로 보아 이분탐색인 것 같은데 접근법이 떠오르지 않음

- 완탐 : 시간초과
    - 이차원 배열에서 대각선을 중심으로 양 날개가 값이 같다는 걸 이용해서, k번째 수를 반환 할 때 순서에 반영한다.
        - 대각선 부분은, 각 (1~n) * (1~n) 한 값이므로 k//n해서 그 값 만큼 더해주고,
    - 값을 채울 때 배수인것들도 넣고, 배수를 채웠다는 것은 1 ~ N 의 일차원 배열 visited를 이용한다.
- 이분탐색
    - 정의 : 전체 숫자 중에서 B[k] 보다 작거나 같은 숫자가 k개보다 작으면 찾는 숫자 범위를 큰 쪽으로 옮긴다.
    - 해당 범위 에서 B[k] 보다 작거나 같은 숫자를 찾는 방법
        - 각 값은 i * j 이므로
        - 이진탐색이 지정한 S을 기준으로  i(1 ~ n)의 각 행에서 min(i, S/i)
"""
import sys
input = sys.stdin.readline

def count_is_smaller_than_target(mid):
    count = 0
    for i in range(1,N+1):
        count += min(N,mid//i)
    # print(f'count_is_smaller_than_target : {count}')
    return count

N = int(input().rstrip())
K = int(input().rstrip())

start = 1
end = K # B[K]는 K보다는 작다
result = 0
while start <= end :
    mid = (start + end) // 2
    # print(f'mid : {mid} 탐색 시작')
    if count_is_smaller_than_target(mid) < K :
        start = mid + 1
        # print(f'mid : {mid} -> [true] start : {start}')
    else :
        result = mid
        end = mid - 1
        # print(f'mid : {mid} -> [false] result : {result}, end : {end}')

print(result)