"""
== 문제 조건
- 코스는 요리가 2개 이상
- 2명 이상의 주문이 있었어야 함
- 코스 요리의 요리 개수는 input으로 정해짐
== 답안 제출 유위 사항 및 엣지케아스
- 최종 제출 할 코스의 목록은 사전 순 오름차순으로 정렬
- WX, XW 가 다른 코스로 인식 되는 것 ==> 콤비를 우선 정렬해서 저장한다.
"""
from itertools import combinations
def is_full_menu(example, customer):
    for menu in example:
        if menu not in customer:
            return False
    return True
def solution(orders, course):
    answer = []
    for num in course:
        candis = dict()
        for customer_menu in orders:
            for unsort_cb in list(combinations(customer_menu, num)):
                cb = sorted(unsort_cb)
                if is_full_menu(cb, customer_menu):
                    str_cb = ''.join(cb)
                    # dict에 개수 update하는 부분
                    if candis.get(str_cb):
                        candis[str_cb] += 1
                    else:
                        candis[str_cb] = 1

        # dict 확인해서 제알 많이 나온거 기준으로 정답에 담을 조합 고르는 부분
        sort_candis = sorted(candis.items(), key=lambda x: x[1], reverse=True)
        if not sort_candis or sort_candis[0][1] == 1:  # 가지치기 : 제일 큰 cnt가 1이면 모든 고객 조합에서 한번 밖에 안 나온 것이므로 답이 될 수 없다.
            continue
        else:
            max_cnt = sort_candis[0][1]
            for k, v in sort_candis:
                if v < max_cnt:  # cnt가 제일 큰 값에서 작아지면 정답에 넣는걸 멈추고 바로 다음 숫자의 조합으로 넘어가게 한다.
                    break
                answer.append(k)

    return sorted(answer)

