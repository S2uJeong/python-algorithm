def same_max_cnt(p_list):
    max_cnt = -(1e10)
    max_num = 0
    for num in p_list:
        cnt = 0
        for j in p_list:
            if num == j :
               cnt += 1
        if cnt > max_cnt :
            max_cnt = cnt
            max_num = num
        elif cnt == max_cnt :
            if max_num < num :
                max_num = num
    return max_cnt, max_num

def first_try() :
    print("주사위를 던질 사람의 수는?")
    T = int(input())
    prize_list = []
    for case in range(T):
        print(f'던진 주사위의 결과 {case+1} : 공백을 기준으로 한줄로 입력해주세요.')
        nums = list(map(int,input().split()))
        cnt, num = same_max_cnt(nums)
        if cnt > 2 :
            prize_list.append(10000+num*1000)
        elif cnt > 1 :
            prize_list.append(1000+num*100)
        else :
            prize_list.append(num*100)

    return max(prize_list)

print(first_try())
