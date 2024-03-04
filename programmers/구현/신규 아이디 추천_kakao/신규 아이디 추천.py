import re
def solution(new_id):
    # 1. 모든 대문자를 소문자로 치환한다.
    new_id = new_id.lower()
    print(f' [1] {new_id}')
    # 2. 특수기호 빼기
    new_id = re.sub("[^a-z0-9-_.]",'',new_id)
    print(f' [2] {new_id}')
    # 3. 연속된 '.' 하나로
    while(new_id.find('..') != -1) :
        new_id = new_id.replace('..','.')
    print(f' [3] {new_id}')
    # 4. 맨 앞뒤에 '.'이 있으면 제거
    if new_id.find('.') == 0 :
        new_id = new_id[1:]
    if new_id.rfind('.') == len(new_id)-1 :
        new_id = new_id[:len(new_id)-1]
    print(f' [4] {new_id}')
    # 5. new_id가 빈 문자열이면 new_id에 'a'대입
    if len(new_id) == 0 :
        new_id = 'a'
    print(f' [5] {new_id}')
    # 6. 길이 확인
    if len(new_id) > 15 :
        new_id = new_id[:15]
        if new_id.rfind('.') == len(new_id) - 1:
            new_id = new_id[:len(new_id) - 1]
    print(f' [6] {new_id}')
    # 7. 길이 확인 2
    while len(new_id) < 3:
        new_id += new_id[len(new_id) - 1]
    print(f' [7] {new_id}')

    return new_id

print(solution("abcdefghijklmn.p"))