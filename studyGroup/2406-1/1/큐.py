from collections import deque
import sys
input = sys.stdin.readline

N = int(input().rstrip())
dQ = deque()
for _ in range(N):
    command = input()
    if command[0:2] == 'pu':
        dQ.append(command[5:].rstrip())
    elif command[0:2] == 'po':
        if len(dQ):
            print(dQ.popleft())
        else :
            print(-1)
    elif command[0:2] == 'si':
        print(len(dQ))
    elif command[0:2] == 'em':
        if len(dQ):
            print(0)
        else:
            print(1)
    elif command[0:2] == 'fr':
        if len(dQ):
            print(dQ[0])
        else:
            print(-1)
    elif command[0:2] == 'ba':
        if len(dQ):
            print(dQ[-1])
        else:
            print(-1)

