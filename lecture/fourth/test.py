# 입력 받는 값
N = int(input())
meeting_times = [list(map(int,input().split())) for _ in range(N)]

def exam(n,p_list) :
    p_list.sort(key = lambda x : (x[1],x[0]))
    et = cnt = 0
    for s,e in p_list:
        if s >= et:
            et = e
            cnt += 1
    return cnt

print(exam(N,meeting_times))