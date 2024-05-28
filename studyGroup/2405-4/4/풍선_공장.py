import sys
input = sys.stdin.readline
N,M = map(int,(input().split()))
times = list(map(int,input().split()))

def is_full_balloons(sec):
    cnt = 0
    for time in times:
        cnt += (sec//time)
    return cnt >= M

# 이진탐색으로 최적 시간을 찾는다.
start = 0
end = min(times) * M

while start <= end:
    mid = (start+end) // 2
    if is_full_balloons(mid) :
        end = mid-1
    else :
        start = mid + 1

print(start)
