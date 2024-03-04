# 특정 프로세스가 몇 번째로 실행되는지
# 우선순위가 같은 건 오른쪽으로 방향하며 나아갈 때 먼저 나오는 프로세스를 우선 실행

## prior : 우선순위를 나타냄, 숫자가 클수록 더 중요
## location : 대상 프로세스 idx를 나타냄
### return - 대상 프로세스가 몇번째로 실행되는지.

def solution(priorities, location):
    max_val = max(priorities)
    crt_idx = 0
    cnt = 0
    while True:
        # 끝까지 갔으면 다시 맨 처음으로 돌아와서 탐색한다.(왼 -> 오 방향 유지하게 해줌)
        if crt_idx > len(priorities)-1 :
            crt_idx = 0
        print(f'crt_idx :{crt_idx}')

        # 현재 위치의 값이 최대값이면 실행하므로 cnt 를 +1한다.
        if priorities[crt_idx] == max_val:
            cnt += 1
            print(f'{priorities[crt_idx]} == {max_val} , cnt - {cnt}')
            if crt_idx == location:
                return cnt
            priorities[crt_idx] = 0
            max_val = max(priorities)
        crt_idx += 1

        print(f'max_val : {max_val}, crt_idx : {crt_idx}')

def another_solution(prior, l):
    ln = len(prior)
    cur = 0
    cnt = 0
    while True:
        if prior[cur%ln] == max(prior) :
            cnt += 1
            prior[cur%ln] = 0
            if cur%ln == l :
                return cnt

        cur += 1

print(another_solution([1, 1, 9, 1, 1, 1], 0))
