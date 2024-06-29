"""
- 자신의 등수 : 나보다 점수가 큰 사람의 수를 세어 1을 더함
- 최종 등수 : 세 대회의 점수의 합을 기준으로

scores : row - N번째 대회, COL - m번째 사람

"""
import sys

input = sys.stdin.readline

N = int(input().rstrip())
total_for_person = [0] * N
for _ in range(3):  # 대회는 늘 3회이다.
    scores = list(map(int, input().split()))
    pair_scores = []
    for idx, val in enumerate(scores):
        total_for_person[idx] += val
        pair_scores.append((val, idx))

    pair_scores.sort(reverse = True)
    peple_in_grade = [0] * N
    grade = 1
    for idx, val in pair_scores:
        peple_in_grade[idx] = grade
        grade += 1

    print(peple_in_grade)

pair_total = []
for idx, val in enumerate(total_for_person):
    pair_total.append((val, idx))
pair_total.sort(reverse = True)
total_in_grade = [0] * N
grade = 1
for idx, val in pair_total:
    total_in_grade[idx] = grade

print(total_in_grade)

def time_over():
    total_for_person = [0] * N  # idx - person num, value - total_score

    for _ in range(3):  # 대회는 늘 3회이다.
        scores = list(map(int, input().split()))
        for i in range(len(scores)):  # 기준이 되는 사람의 스코어
            total_for_person[i] += scores[i]
            result = 0
            for j in range(len(scores)):  # 비교 되는 나머지 사람들의 스코어
                if scores[i] < scores[j]:
                    result += 1
            print(result + 1, end = ' ')
        print()

    for i in range(len(total_for_person)):
        total_result = 0
        for j in range(len(total_for_person)):
            if total_for_person[i] < total_for_person[j]:
                total_result += 1
        print(total_result + 1, end = ' ')
