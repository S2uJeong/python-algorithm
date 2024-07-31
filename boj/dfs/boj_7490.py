"""
수열의 길이는 1 ~ 9 / + - 공백 3가지 방법
숫자 자릿수 마다 해당 방법들을 사용할 수 있으므로 3^9의 경우의 수가 있으며 테스트 케이스는 10 이므로
자료 양은 3 ^9 * 10 = 200,000   :  O(N)의 방법으로 찾아야 한다.

백트래킹 : 각 노드 상황에서, +, -, 공백으로 선택해서 쭉 나간뒤, 깊이가 주어진 수와 같아지면 계산 결과를 return 한다.
    - 계산 후엔 숫자로만 넘긴다.
    - 출력 시, 아스키코드 정렬 조건이 들어 있어, 공백 - 더하기 - 빼기 순으로 dfs 진행
"""

def dfs(n, sign, calculed_result, crt_num, exp):  # crt_num은 공백계산을 위함
    if n == N :
        calculed_result += (sign * crt_num)  # 마지막 연산이 공백인 경우 감안한 식
        if calculed_result == 0 :
            print(exp)
        return

    dfs(n+1, sign,     calculed_result,              crt_num*10+(n+1), exp+' '+str(n+1))
    dfs(n+1, 1,   calculed_result+sign*crt_num, n+1,              exp+'+'+str(n+1))
    dfs(n+1, -1,       calculed_result+sign*crt_num, n+1,              exp+'-'+str(n+1))


T = int(input())
for _ in range(T):
    N = int(input())
    dfs(1,1,0,1,"1")
    print()

