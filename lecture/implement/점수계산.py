def first_try():
    print("점수를 입력해주세요.")
    scores = list(map(int, input().split()))
    result,cnt = 0,1
    for score in scores:
        if score == 0:
            cnt = 1
        else:
            result += cnt
            cnt += 1
    return result