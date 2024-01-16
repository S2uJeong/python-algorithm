# 아이디어 : 끝나는 시간으로 정렬을 해야 (회의가 빨리 끝나는) 한다.
    # 오답노트 : 1. 아이디어를 잘못 떠올린것 같다 -- 정렬을 생각하긴 했는데,, 빨리 끝나는게 어떤 효과가 있을지 생각 못함
#              2. 시간이 24시간 이후로도 나올 수 있을지 예상 못함 (이건 문제 잘못 아니냐구요!!!)

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



t_list = []

min = 1e10
res= 0
time_list = [0] * 26 # 24시간
# 회의 시작 시간 기준으로 정렬한다.
meeting_times = sorted(meeting_times, key = lambda x : x[0])
# 회의 시간이 짧은 순으로 회의를 잡는다.
   # 현재 idx를 만들어서, 시간테이블을 조정
   # cnt로 회의 개수를 센다.
for idx,time in enumerate(meeting_times):
    tmp = time[1] - time[0] # 걸리는 시간  (meeting_times에서 해당 회의의 인덱스 : 걸리는 시간)
    t_list.append((idx,tmp))

print(f' 미팅시간 : {meeting_times}')
t_list = sorted(t_list, key = lambda x : x[1])
print(f't : {t_list}')

for t in t_list:
    if 1 not in time_list[meeting_times[t[0]][0]:meeting_times[t[0]][1]] :
        res += 1
        for j in range(meeting_times[t[0]][0],meeting_times[t[0]][1]):
            time_list[j] = 1
    else:
        continue
    print(f't : {t} ----- res : {res}, time_list : {time_list}')

print(res)

