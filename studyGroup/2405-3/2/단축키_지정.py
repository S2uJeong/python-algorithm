"""
- 리스트는 재정의 가능, 문자열은 재정의 불가능
- 리스트는 index_초과 에러 있음, 문자열은 없음 (인덱싱 할 때 자유롭게 사용가능)

"""
def solution(result) : # turn 마다 result 리스트 받고, char_list 반환한다.
    char_list = input().split()

    # 1. 각 단어의 첫 문자 확인
    for i,chars in enumerate(char_list):
        if chars[0].lower() not in result:
            result.append(chars[0].lower())
            char_list[i] = '[' + chars[0] + ']' + chars[1:]
            return char_list
    # 2. 만약 각 단어 첫 문자에서 키워드가 안 나오면 처음부터 끝까지 확인
    for i,chars in enumerate(char_list):
        for j in range(1,len(chars)):
            if chars[j].lower() not in result:
                result.append(chars[j].lower())
                char_list[i] = chars[0:j] + '[' + chars[j] + ']' + chars[j+1:]
                return char_list
    # 3. 끝내 없으면 원래 문자 반환
    return char_list

T = int(input())
result = []  # 소문자 기준으로 이미 나온 키워드들이 들어간다.
for _ in range(T):
    answer_list = solution(result)
    for chars in answer_list:
        print(chars, end=' ')
    print()
