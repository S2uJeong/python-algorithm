"""
https://school.programmers.co.kr/learn/courses/30/lessons/42748
"""
def solution(array, commands):
    answer = []
    for i,j,k in commands:
        cut_array = array[i-1:j]
        cut_array.sort()
        answer.append(cut_array[k-1])

    return answer
