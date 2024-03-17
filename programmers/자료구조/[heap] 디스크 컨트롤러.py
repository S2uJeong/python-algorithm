"""
lv3
https://school.programmers.co.kr/learn/courses/30/lessons/42627
"""

import heapq

def solution(jobs):
    start, crt_sec, cnt_job, answer =  -1, 0, 0,0
    hp = []  # 힙 자료구조, 대기중인 작업이 삽입된다.

    jobs.sort(key=lambda x: x[1])  # 소요시간이 짧은 작업순으로 오름차순 정렬

    # 한 반복에 하나의 작업만 처리 해야함.
    while cnt_job < len(jobs):
        # 현 시점 대기중인 작업 삽입
        for i in range(len(jobs)):
            # 대기 중인 작업의 요청 시간은 이전 작업의 요청 시간보다는 크고, 현재 시간보다는 작거나 같아야한다.
            if start < jobs[i][0] <= crt_sec:
                heapq.heappush(hp, [jobs[i][1],jobs[i][0]])
        # print(hp)
        # 대기중인 작업 중에서 시작 시간이 제일 짧은 작업이 수행된다.
        if hp :
            tmp_time = heapq.heappop(hp)
            # print(f' This is log = {tmp_time}')
            start = crt_sec
            crt_sec += tmp_time[0]
            cnt_job += 1
            answer += crt_sec - tmp_time[1] # 작업 완료 시간 - 각 작업의 요청시간 = 수행하는데 걸린 시간
        else :
            crt_sec += 1
    return int(answer / len(jobs))

jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))