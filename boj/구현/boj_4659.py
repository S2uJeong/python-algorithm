import sys
input = sys.stdin.readline

def print_answer(word, is_acceptable):
    result = ''
    if is_acceptable:
        result = 'is acceptable'
    else :
        result = 'is not acceptable'
    print(f'<{word}> {result}.')


def is_security(password):
    moum = ['a','e','i','o','u']
    one_moum_result = False # 모음이 하나라도 들어갔다.
    # 같은 종류 글자 3개 연속 조건
    jaum_count = 0
    moum_count = 0
    # 같은 글자 두번 연속 불가
    for i in range(len(password)):
        if password[i] not in moum:
            jaum_count += 1
            moum_count = 0
        else :
            one_moum_result = True
            moum_count += 1
            jaum_count = 0

        if jaum_count == 3 or moum_count == 3 :
            return False

        if is_success_word(password, i):
            return False

    if one_moum_result:
        return True

    return False

def is_success_word(password, char_idx):
    if char_idx == 0 :
        return False

    if password[char_idx] == password[char_idx-1]:
        if password[char_idx] not in ['e','o']:
            return True

    return False


while True:
    password = input().rstrip()
    if password == 'end':
        break
    print_answer(password, is_security(password))