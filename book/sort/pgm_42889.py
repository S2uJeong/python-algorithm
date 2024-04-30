"""
- stages 배열로 들어오는 숫자는, 도전할 스테이지의 번호이며 N+1의 스테이지는 스테이지를 다 클리어 했다는 말
- stages는 연속적이므로, 4는 1,2,3을 이미 깼다는 것
1. for i in range(1,N);총 스테이지 를 돌며 해당 스테이지에서 실패율을 구한다.
2   for j in stages를 선형탐색하다가 i보다 큰 값이면 실패율을 idx를 통해 구하고 result에 넣고 작으면 pass한다.
    - 조건 :  stages는 오름차순 정렬되어 있다.
"""
def soluton(N,stages):
    result = []
    length = len(stages)

    for i in range(1,N+1):
        # 해당 스테이지에 머물러 있는 사람의 수
        count = stages.count(i)

        # 실패율 계산
        if length == 0 :
            fail = 0
        else :
            fail = count / length

        result.append((i,fail))
        length -= count

    result.sort(key = lambda x : -x[1])
    result = [i[0] for i in result]
    return result

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(soluton(N,stages))