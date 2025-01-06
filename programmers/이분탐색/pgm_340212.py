"""
제한 시간 내에 퍼즐을 모두 해결하기 위한 [숙련도의 최솟값]을 구하기

1. limit의 범위가 크기 때문에 최소값을 구하기 위한 그리디한 방법이 있을지 고민
2. 그리디한 방법이 없으면 숙련도를 기준으로 이분탐색을 한다 (max : 퍼즐의 최대 난이도 (100_000))

놓친 부분 : 숙련도도 양의 정수여야 합니다.
"""
# 단일 문제, 숙련도에 대해 문제를 푸는데 걸린 시간을 반환한다.
def cal_solve_time(level, diff, solve_time, pre_time): # 첫번째 퍼즐의 경우 pre_time을 0으로 설정
    wrong_cnt = max(diff - level, 0)
    return (solve_time + pre_time) * wrong_cnt + solve_time

def solution(diffs, times, limit):
    left = 0
    right = max(diffs) # 100_000 퍼즐의 최대 난이도를 숙련도의 max값으로 지정
    answer = right
    while left <= right:
        level = (left + right) // 2
        sum_solve_time = cal_solve_time(level, diffs[0], times[0], 0)
        for i in range(1,len(diffs)):
            sum_solve_time += cal_solve_time(level, diffs[i], times[i], times[i-1])

        if sum_solve_time > limit:
            left = level + 1
        else:
            right = level - 1
            answer = min(answer, level)

    return max(1,answer) # 숙련도는 양의 정수여야 한다.
