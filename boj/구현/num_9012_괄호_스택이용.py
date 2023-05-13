import sys
input = sys.stdin.readline
print = sys.stdout.write

for _ in range(int(input())):
    stack = []
    str_list = input().split()

    for i in str_list[0]:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else:
                print("NO")
                break

    else: # 🔴 for문과 같은 라인에 있는 else : for문이 break문 없이 끝난 후 수행할 명령
        if not stack: # 스택이 비어있다.
            print("YES")
        else:
            print("NO")