"""
1. 바뀐 뒤 결과가 되는 문자열인 T의 맨 뒤부터 시작한다.
2. 맨 끝 글자가 A이면 A를 빼고
   맨 끝 글자가 B이면 먼저 뒤집고, 맨 앞의 B를 뺀다.
3. 글자가 S의 길이만큼 남을때까지 반복하고, S와 T가 같은지 확인한 뒤 결과를 반환한다.

간과한것
처음엔 dfs없이 while 문을 이용해서 t 길이가 S와 같아질때 까지 str을 빼주고
결과가 S와 같으면 1, 아니면 2를 반환하려 했는데 조건문이 복잡해지고 A,B 둘 다 빼기 가능한 상황일때
어떤걸 우선으로 할까 생각하다가 두 경우 다 탐색할 수 있는 dfs 도입
"""

S = input()
T = input()

result = 0
def dfs(t):
    global result
    if t == S :
        result = 1
        return
    if len(t) == 0:
        return
    # 뒤가 A거나 앞이 B가 아닌 것들은 S로 만들 수 없다.
    if t[-1] == 'A':
        dfs(t[:-1])
    if t[0] == 'B':
        dfs(t[1:][::-1])

dfs(T)
print(result)
