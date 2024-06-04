"""
1. 회의 소요 시간이 적은 회의들로 부터 스케줄을 구성하면,배정되는 회의의 수는 늘어난다 !  -> 첫번째 아이디어 -> 틀림
2. 끝나는 시간이 이를수록 회의를 많이 할 수 있다.
=> 그리디를 정렬로 생각할 때, 정렬의 기준이 되는 것을 여러개 생각해서 되는지 각자 생각해보고 시작하는게 좋을 듯
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
times = [list(map(int, input().split())) for _ in range(N)]
times.sort(key = lambda x : (x[1],x[0])) # 끝나는 시간, 시작 시간을 기준으로 정렬

current = 0
result_cnt = 0
for S,E in times:
    if current <= S:
        result_cnt += 1
        current = E
print(result_cnt)


