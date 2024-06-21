"""
최대 HP의 최소값 구하기  ->  최단 경로 ?

6 * 3 의 자리수 만큼 최대 필요할 수 있음 HP가
( 방의 개수 * 몬스터의 HP * 용사의 공격력이 1일 때 몬스터를 죽일때까지의 최대 횟수 )
"""
import sys
input = sys.stdin.readline

N, A = map(int,input().split())
commands = [list(map(int,input().split())) for _ in range(N)]

result = 0
start = 1
end = N * int(1e6) * int(1e6)
while start <= end :
    flag = True # 해당 HP로 몬스터를 무찌를 수 있는가
    mid = (start + end) // 2
    crt_hp = mid
    crt_attack = A
    for t,a,h in commands:
        if t == 1: # 몬스터면
            # x로 현재 공격력으로 몬스터를 죽일 때까지 횟수를 구함
            x = 0
            if h % crt_attack == 0 :
                x = h // crt_attack
            else :
                x = (h // crt_attack) + 1
            # 용사의 현재 hp가 용의 공격력과 해치우는데 걸리는 횟수를 곱한거 보다 작거나 같으면 패배
            if crt_hp <= (a*(x-1)) :  # 용사가 먼저 공격하므로, 횟수를 1 빼준다.
                flag = False
                break
            crt_hp -= (a*(x-1))
        else : # 포션이면
            crt_hp = min(mid, crt_hp + h)
            crt_attack += a

    if flag :
        # for문을 무사히 돌았으면 result 업데이트 !
        result = mid
        end = mid - 1 # 더 작은 값을 구해 볼 수 있도록 조정
    else :
        start = mid + 1

print(int(result))
