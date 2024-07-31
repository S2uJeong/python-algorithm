import sys
input = sys.stdin.readline
def select_char(cnt):
    result = ''
    if cnt == 0 :
        return 'dot'
    if cnt >= 4 :
        result += ('AAAA' * int(cnt/4))
        cnt -= (4 * int(cnt/4))
    if cnt >= 2 :
        result += ('BB' * int(cnt / 2))
        cnt -= (2 * int(cnt / 2))
    if cnt :
        return ''
    else :
        return result


input_string = input().rstrip()

cnt = 0
result = ''
for c in input_string:
    if c == '.':
        result_char = select_char(cnt)
        cnt = 0
        if result_char :
            if result_char == 'dot':
                result += '.'
            else:
                result += result_char
                result += '.'
        else :
            print(-1)
            exit()
    else :
        cnt += 1

if cnt :
    result_char = select_char(cnt)
    if result_char:
        result += result_char
        print(result)
    else:
        print(-1)
else :
    print(result)