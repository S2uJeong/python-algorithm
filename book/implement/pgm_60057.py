"""
문자열 압축 - https://school.programmers.co.kr/learn/courses/30/lessons/60057
"""
def mySolution(s):
    str_list = []
    result = 0
    answer = -124023580
    # s의 길이 반절까지만 탐색한다. (i : 갯수를 의미 )
    for i in range(1, len(s)//2):
        # (j : 리스트 안에 탐색)
        for j in range(i, len(s), i):
            # 나머지 남으면 바로 더해주기
            if len(s) - j < i :
                result += len(s) - j
                return result
            tmp_str = s[(j-i):j]
            # 만약 언어 리스트에 있는 문자열이면, 추가 안한다.
            # 없다면, 숫자까지 고려하여 글자수 +1 을 더해준다.
            if tmp_str not in str_list :
                str_list.append(tmp_str)
                result += i+1
        if answer > result :
            answer = result
    return answer

def solution(s) :
    answer = len(s)
    for step in range(1,len(s)// 2 +1):
        compressed = ""
        prev = s[0:step]
        count = 1
        # 단위 만큼 증가 시키며 이전 문자열과 비교
        for j in range(step, len(s), step):
            # 이전 상태와 동일하다면 압축 횟수(cnt) 증가
            if prev == s[j:j + step]:
                count += 1
            # 다른 문자열이 나왔다면
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j+step] # 상태 초기화
                count = 1
        # 남아 있는 문자열 처리
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))
    return answer
