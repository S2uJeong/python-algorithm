""" [성공]
1. 1의 자리수부터 시작한다.
2. 조건문 검증
2-1 현재 수가 0~4이면 해당 자리수만큼 (-1) 하는것이므로 횟수로 더해준뒤, 몫을 다음수로 넘긴다.
2-2 현재 수가 6~9이면 (10 - cur) 만큼 횟수로 더해주고, 몫에 10을 더해 넘긴다.
2-3 현재 수가 5이면 다음 자릿수에 따라 2-1 or 2-2를 실행한다.
"""
def solution(storey):
    answer = 0
    while storey:
        rest = storey % 10   #나머지

        if rest <= 4:
            answer += rest

        elif rest >= 6:
            answer += (10-rest)
            storey += 10

        else: # 5일 때 (올림, 반올림 선택은 그 앞자리에 따라)
            if((storey // 10) % 10) >= 5:
                storey += 10
            answer += rest

        storey //= 10
    return answer

""" [실패] 
현재의 수를 제일 높은 자리 수 기준으로 반올림을 한뒤, 버려지거나 남는 수를 가지고 또 반복한다.
    1. 기준이 됐던 높은 자리 수는, 반올림 결과에 따라 횟수로 더해준다.    ex) 345 -> 300 이면 3을 (-100*3) 결과에 더해주고
    2. 버려지거나 남는 수를 dfs에 돌린다.
=> 실패 케이스 999 등, 정당성 검증 실패
"""
def dfs(cur_num_string):
    global result

    pivot = int(cur_num_string[0])
    print(f'pivot : {pivot}')
    if len(cur_num_string) <= 1:
        result += min(pivot, 10 - pivot + 1)
        return
    next_part = cur_num_string[1:]

    if pivot >= 6 :
        result += (10 - pivot + 1)  # 10-pivot은 자릿수 올리기 위한 +의 횟수고, +1은 올린 자릿수 만큼 한 번에 빼주는 횟수.
        next_num = ((len(cur_num_string)+1) * 10) - int(next_part) # 다음 수를 구하는 식.
    else:
        result += pivot
        next_num = int(next_part)

    print(f'result : {result}')
    dfs(str(next_num))

def solution_fail(storey):
    result = 0
    dfs(str(storey))
    return result

