"""
1. 스위치 순서 대로 해당 스위치가 켤 수 있는 램프를 집합 자료구조에 넣는다.
2. N-1번째 턴까지 집합 자료구조의 길이가 램프의 길이와 같아지면 램프를 모두 켤 수 있다
스위치를 차례로 할 수 있는 이유 : 스위치 순서 상관 없이 다 켜져야 하기 때문
오답 : 어떤 스위치를 어떤 순서로 누를 지 모른다
===============================
1. 콤비네이션을 통해 스위치 N-1개를 뽑는 경우를 다 뽑는다.
2. 해당 스위치를 눌렀을때 램프가 다 켜지는지 확인
3. set 자료구조 사용
4. 성능개선 : 다 보기 전에 이미 set의 길이가 M이 됐을 떄 .
오답 : 왜 오답이지? 문제를 잘못 이해했나.
===============================
아이디어 : 모든 램프가 켜져 있다고 가정하고 풀이, 램프를 눌린 횟수로 저장
이렇게 가정하고 풀면 한 번의 스위치 확인으로도 N-1번 눌렀을 때 모두 켜지는지 확인이 가능하다.
"""

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
lamps = [list(map(int,input().split()))[1:] for _ in range(N)]

# 램프별 몇번 눌렸는지 update
lamp_cnt = [0] * (M + 1)
for lamp in lamps:
    for l in lamp:
        lamp_cnt[l] += 1
def is_turn_off(lamps, tmp_lamp_cnt):
    for off_idx in lamps:
        tmp_lamp_cnt[off_idx] -= 1
    if 0 in tmp_lamp_cnt[1:]:
        return False  # 꺼진 램프가 존재 한다.
    else :
        return True

answer = 0
for i in range(N):    # 스위치 별로 확인
    answer = 0
    tmp_lamp_cnt = lamp_cnt[:]  # 🔴🔴🔴🔴
    tmp = is_turn_off(lamps[i], tmp_lamp_cnt)
    #print(f'bool_result : {tmp}')
    ##print(f'lamp_cnt : {lamp_cnt}')
    #print(f'lamp_cnt_tmp : {tmp_lamp_cnt}')
    if tmp == True :
       answer = 1
       break

print(answer)


