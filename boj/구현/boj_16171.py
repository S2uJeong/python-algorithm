import sys
input = sys.stdin.readline

data = input().rstrip()
target = input().rstrip()
result = []

for d in data:
    if ord('A') <= ord(d) <= ord('Z') : #대문자인지
        result.append(d)
    elif ord('a') <= ord(d) <= ord('z'): #소문자인지
        result.append(d)

result = ''.join(result)

if target in result:
    print(1)
else :
    print(0)