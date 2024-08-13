import sys
input = sys.stdin.readline

def check_string(string):
    stack = []
    for ch in string:
        #print(stack)
        if ch in '[(':
            stack.append(ch)
        elif not stack and ch in '])':  # '(' 만 들어온 경우
            return False
        elif stack and ch == ']' :
            if stack.pop() != '[':
                return False
        elif stack and ch == ')':
            if stack.pop() != '(':
                return False
    if len(stack):
        return False  # '(' 만 들어온 경우
    return True

while True:
    string = input().rstrip()
    if string == '.':
        break
    if check_string(string):
        print('yes')
    else:
        print('no')


