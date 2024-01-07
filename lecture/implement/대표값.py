# 절댓값 구하는건 math 라이브러리 필요 없이 abs()로 가능하다.
# 어떤 값의 기준으로 차이를 계산 할 때에는 절댓값 처리 해주는거 주의.

n = int(input())
score_list = list(map(int,input().split()))

average_score = int(round(sum(score_list) / len(score_list),0))

# 평균과 점수들의 최소 차이 수 구하기
## 🔴 해당 부분에서 abs() 처리 해주지 않아 버그가 발생했다.
score_diff = 0
for score in score_list:
    if abs(average_score - score) < score_diff :
        score_diff = abs(average_score - score)

result_list = []
for i,score in enumerate(score_list):
    if average_score - score == score_diff:
        result_list.append((i+1,score)) # 문제에서 학생 번호를 1~N으로 제시하였기에 i+1로 반영함.

sorted_list = sorted(result_list, key = lambda x: (-x[1],x[0]))
print(average_score, sorted_list[0][0])

def first_try(score_list):
    average_score = int(round(sum(score_list) / len(score_list), 0))

    # score_diff : 평균과 점수들의 최소 차이 수 구하기
    score_diff = 0
    for score in score_list:
        if abs(average_score - score) < score_diff:
            score_diff = abs(average_score - score)

    result_list = []
    for i, score in enumerate(score_list):
        if average_score - score == score_diff:
            result_list.append((i + 1, score))  # 문제에서 학생 번호를 1~N으로 제시하였기에 i+1로 반영함.

    sorted_list = sorted(result_list, key=lambda x: (-x[1], x[0]))
    return average_score, sorted_list[0][0]

score, num = first_try([12,34,17,6,11,15,27,42,39,31, 25, 36, 35, 25, 17])
print(score, num)

# 주어진 조건을 풀려고 하지 않아도, 넘어가는것으로도 충족할 수 있다는 것을 보여줌..!
def example(v_list):
    average_score = round(sum(v_list)/len(v_list))
    min = 2324349320594

    for idx, score in enumerate(v_list):
        tmp = abs(score - average_score)
        if tmp < min:
            min = tmp
            o_idx = idx +1
            o_score = score
        elif tmp == min:
            if score > o_score :
                o_idx = idx +1
                o_score = score
    return average_score, o_idx

score, num = example([12,34,17,6,11,15,27,42,39,31, 25, 36, 35, 25, 17])
print(score, num)