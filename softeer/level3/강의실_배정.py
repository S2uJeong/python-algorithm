import sys
input = sys.stdin.readline

N = int(input().rstrip())
courses  = [list(map(int,input().split())) for _ in range(N)]
courses.sort(key = lambda x : x[1])

count = 0
cur_time = courses[0][0]
for start, end in courses:
    if start >= cur_time:
        count += 1
        cur_time = end

print(count)