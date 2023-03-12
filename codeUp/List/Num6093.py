total = int(input());
callList =list(map(int, input().split()));

answer = [];
for i in range(total-1,-1,-1):
    answer.append(callList[i]);

print(*answer);