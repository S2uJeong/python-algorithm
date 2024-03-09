"""
https://school.programmers.co.kr/learn/courses/30/lessons/42840
"""
def solution(answers):
    a_answers = [1,2,3,4,5]
    b_answers = [2,1,2,3,2,4,2,5]
    c_answers = [3,3,1,1,2,2,4,4,5,5]
    grades = [0,0,0]
    for i in range(len(answers)):
        if answers[i] == a_answers[i%len(a_answers)]:
            grades[0] += 1
        if answers[i] == b_answers[i % len(b_answers)]:
            grades[1] += 1
        if answers[i] == c_answers[i%len(c_answers)]:
            grades[2] += 1

    max_grade = max(grades)
    answer = []
    for i in range(len(grades)):
        if grades[i] == max_grade:
            answer.append(i+1)

    return answer

# print(solution([1,3,2,4,2]))