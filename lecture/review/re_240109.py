# 1. 자릿수의 합
def digit_sum(p_num):
    sum = 0
    while p_num > 0 :
        sum += p_num % 10
        p_num = p_num // 10

    return sum

#print(digit_sum(19))

# 2. 소수의개수
def prime_cnt(p_num):
    cnt = 0
    nums = [0]*(p_num + 1)
    for i in range(2,p_num+1):
        if nums[i] == 0 :
            cnt += 1
            for j in range(i,p_num+1,i):
                nums[j] = 1
    return cnt

#print(prime_cnt(5))


# 3. 대표값
# 전역변수 줄일 것
def represent() :
    print("점수 리스트를 공백을 기준으로 한 줄에 적어주세요")
    scores = list(map(int,input().split()))
    avg = int((sum(scores) / len(scores)) + 0.5)
    # scr_max = -(1e10)
    diff_min = 1e10
    # result = 0
    for idx, score in enumerate(scores):
        if abs(score - avg) < diff_min :
            diff_min  = abs(score - avg)
            o_idx = idx+1
            o_score = score
        elif abs(score - avg) == diff_min :
            if score > o_score:
                o_idx = idx+1
                o_score = score
    return avg, o_idx

# print(represent())

# 4. 파이썬 반올림 (even법) 대응 함수
def halfround(p_num) :
    return int(p_num+ 0.5)