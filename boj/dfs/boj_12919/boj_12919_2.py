"""
뒤에 A 추가 or 뒤에 B 추가 + 문자열 뒤집

완성본을 기준으로 매회마다 두 방법을 전개해서 안되는건 return
글자가 하나씩 없어지고, S 길이와 T 길이 같을 떄, S==T인 경우가 있으면 true

최대 50글자이고, 글자 하나씩 없어질 때 마다 2가지 방법이 전개 되므로 2^50이므로 경우의 수가 너무 많다.
- 가지치기 방법
    1. 이미 나왔던 경우라면 탐색하지 않음
    2. 반대로 돌기 때문에 2가지 방법 중 하나를 선택했을 때 수행할 수 없는 경우가 생김. 그땐 바로 return
        - A 추가 경우 : 맨 뒤글자가 A가 아니면 return
        - B추가 + 뒤집 : 맨 앞글자가 B가 아니면 return
"""
S,T = input(), input()

result = 0
def dfs(cur_chars):
    global result
    if result :
        return

    if len(cur_chars) == len(S):
        if cur_chars == S:
            result = 1
        return

    if cur_chars[-1] == 'A':
        #print(f'A : {cur_chars[:-1]}')
        dfs(cur_chars[:-1])

    if cur_chars[0] == 'B':
        #print(f'B : {cur_chars[1:][::-1]}')
        dfs(cur_chars[1:][::-1])


dfs(T)
print(result)