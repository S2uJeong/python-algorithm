from collections import deque
def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    res = []

    while progresses :
        cnt = 0
        # 완성도가 100이면 큐에서 내보낸다.
        if progresses[0] == 100:
            while progresses :
                if progresses[0] >= 100 :
                    progresses.popleft()
                    speeds.popleft()
                    cnt += 1
                else :
                    break
        # 날이 지날때마다 프로세스들의 진행도 update
        else :
            for idx, val in enumerate(progresses):
                progresses[idx] = val + speeds[idx]

        if cnt > 0 :
            res.append(cnt)
    return res


progress = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
print(solution(progress, speeds))


