"""
모든 주전자의 막걸리 양을 더한뒤, 명수로 나눠 평균을 구한다.
0 ~ 평균값 사이에서, 이분탐색을 하며 주전자 용량이 동 나지 않는지 확인한다.
    - 주전자 하나에서 따르다가 끊기면 해당 주전자는 버리고 다음으로 이어지는 로직 구현
"""
import sys
input = sys.stdin.readline

N,K = map(int, input().split())
bowls = [int(input().rstrip()) for _ in range(N)]
result = 0
if sum(bowls) >= K: # 🔴 막걸리 합이 K(명)을 못 넘으면 답은 0
    start = 1 # 🔴 답이 0일 때를 이미 제외했기 때문에 1로 시작한다.
    end = sum(bowls) // K  # 최대량은 총 막걸리 용량의 인원수를 나눈 몫보다 클 수 없다.
    while start <= end:
        mid = (start + end) // 2  # 🔴start를 0으로 했으면 zeroDivision에러뜰 수 있음. 위에서 가지치기해서 가능
        # mid양대로 주전자 잔 따르기
        cnt = 0  # 잔을 받은 친구 수
        for i in range(len(bowls)):
            tmp = bowls[i]
            cnt += (tmp // mid)
        # 결과에 따라 이분탐색 조정
        if cnt >= K:
            result = max(result, mid)
            start = mid+1
        else :
            end = mid-1

print(result)