"""
탑승한 사람의 무게와 시소 축과 좌석 간의 거리의 곱이 양쪽 다 같다면

100_000 (사람 무게) * 3 (2/3/4m) 곱해서 나올 수 있는 모든 경우의 수를
=> 같은 사람으로 셀렉되지 않는다는 확신이 어떻게 있지? => 매칭 해준 다음 해당 숫자 만큼을 다 빼준다.

1. 무게를 idx로 해서 (최대 몸무게 1_000) 해당 무게를 가진 사람이 몇 명인지 value로 업데이트 한다.
2. 무게 자료구조를 set으로 바꿔서, 같은 무게면 한 번만 계산 되도록 최적화한다.
3. 무게 set을 for문으로 돌며
    - 해당 무게에 대해 memo val -1 을 해서 같은 사람이 고려 짝궁으로 고려되지 않도록 제외한다.
    - for (2,3,4)
      tmp = 해당 무게 * i
        - for (1,2,3,4)
            if (tmp % j == 0) :
            memo idx가 tmp // j 인 val의 값을 result에 더해준다.
"""
def solution(weights):
    answer = 0
    memo = [0] * 4001 # 시소추가 반영된 몸무게는 1_000  * 4 의 값을 최대로 가진다.

    for w in weights:
        memo[w] += 1

    for weight in weights:
        memo[weight] -= 1

        visited = [0] * 4001
        for i in (1,2,3,4):
            cal_weight = weight * i
            for j in (1,2,3,4):
                if cal_weight % j == 0:
                    if memo[cal_weight // j] and not visited[cal_weight // j]:
                        # print(f'answer 올라간다 ===== weight: {weight}, cal_weight: {cal_weight}, memo idx: {cal_weight // j}')
                        answer += memo[cal_weight // j]
                        visited[cal_weight // j] = 1
    return answer


