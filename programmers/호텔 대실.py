# https://school.programmers.co.kr/learn/courses/30/lessons/155651

# 시간 테이블 관련 활용 -> 자료구조는 리스트 이용
# 2차원 리스트를 시,분으로 만들어서 그게 1로 채워져 있으면, cnt 늘리고, 아닌 부분 1로 채워준다.
    # 🔴-> 2차원 리스트로 하지 않고, 0 ~ 2359로 만들어서 표시한다.🔴

# 조건
# 1. 방 준비시간이 10분 걸린다.
 # -> 시간 받은 걸로, 시작 시간 ~ 방 준비시간 + 10분 까지의 idx에 해당하는 값에 1더한다. (처음 초기화는 0으로)
# 2. 1을 더한 뒤, 2359 리스트에서 제일 큰 값을 구하면 동시에 필요한 방의 갯수를 알 수 있다.
book_time = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]

def solution(book_time):
    # HHMM 형식의 글자를 1200 식으로 변환해주는 함수
    def trans(HHMM):
        time = HHMM[0:2] + HHMM[3:5]
        return int(time)
    # idx는 24시간 표기법의 시간을 뜻하며 시간에 따라 사용되고 있는 방의 갯수를 값으로 가지고 있다.
    time_list = [0] * 2359

    for stime, etime in book_time:
        stime = trans(stime)
        etime = trans(etime)
        for i in range(stime, etime+10):  #방 정리하는데 10분 걸림
            time_list[i] += 1

    return max(time_list)









    return 0
