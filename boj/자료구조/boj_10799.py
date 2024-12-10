"""
시간복잡도 계산 : O(n)

스택을 사용하는 이유 : 괄호의 열고 닫히는 구조를 추적할 수 있는 자료구조
'(' 일 땐 스택에 추가하고, ')'가 나타나면 제거하여 현재 상태를 쉽게 추적
"""
inputs = list(input())
sticks = [] # 여는 괄호를 넣는다.
result = 0

for i in range(len(inputs)):
    if inputs[i] == '(':
        sticks.append('(')
    else:
        if inputs[i-1] == '(': # 레이저 발견
            sticks.pop()
            result += len(sticks)
        else: # )) 이므로 막대기 확실
            sticks.pop()
            result += 1

print(result)

