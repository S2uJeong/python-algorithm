# 1. str.upper() : 대소문자를 가리지 않을 때 사용
# 2. for-else : for문이 break 등으로 중간에 빠져나오지 않으면 진행된다.
# 3. 파이썬의 문자열 비교 : ==,!=
# 4. len(list)//2 수식으로 idx절반 활용하는 방법
    # - 홀수일땐, 가운데 idx 뺴고 탐색, 짝수일땐 딱 반절까지

def first_try():
    T = int(input())
    input_list = []
    for _ in range(T):
        tmp = input().upper()
        input_list.append(tmp)
    for idx, s in enumerate(input_list):
        if s == s[::-1]:
            print(f'#{idx + 1} YES')
        else:
            print(f'#{idx + 1} NO')

def example():
    T = int(input())
    for i in range(T):
        s = input()
        s = s.upper()
        for j in range(len(s)//2):
            if s[j] != s[-j-1] :
                print(f'#{i + 1} NO')
                break
        else:
            print(f'#{i + 1} YES')
