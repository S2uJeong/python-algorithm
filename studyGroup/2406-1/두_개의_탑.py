"""
st, ed 로 두 포인터 설정 하고, n * n 조합으로 for문을 돌며 두 포인터의 차이가 큰 값을 업데이트한다. => index로 시도했으나 선형 탐색 후 방향 뒤쪽으로 탐색하는게 안됨
point : 누적합을 통해 거리를 구해준다.
50,000 * 50,000 = 1,000,000,000
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
distanse = [0] + [int(input().rstrip()) for _ in range(N)]
# 누적합 생성
presum = [0] * (N+1)
for i in range(1,N+1):
    presum[i] = presum[i-1] + distanse[i]

result = 0
for i in range(1,N+1):
    st, ed = i, N
    while st <= ed :
        mid = (st+ed)//2
        # 🔴 누적합으로 시계방향/반시계방향 구하는 부분
        value = presum[mid] - presum[i-1]
        reverse_value = presum[N] - value

        min_value = min(value,reverse_value)
        result = max(result, min_value)

        if (value < reverse_value) : # 반 시계 방향이 커지면, 시계방향은 계속 작아진다.
            st = mid + 1
        else :
            ed = mid - 1

print(result)
