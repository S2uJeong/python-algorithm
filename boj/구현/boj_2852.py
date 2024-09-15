"""
시간 계산 문제여서, 초-분 환산을 미리 하는게 point
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())

goal_info = []
for _ in range(N):
    goal_team, goal_time = input().split()
    goal_team = int(goal_team)
    goal_time_m, goal_time_s = map(int,goal_time.split(":"))
    goal_time = goal_time_m * 60 + goal_time_s # 초로 환산
    goal_info.append((goal_time, goal_team))

goal_info.append((48 * 60, 0)) # 끝 시간을 넣어준다.
goal_info.sort() # 골을 넣은 시간 오름차순 정렬

team_score = [0,0,0] # idx : 팀 숫자
winning_time = [0,0,0]

for i in range(len(goal_info)-1):
    goal_time, goal_team = goal_info[i][0], goal_info[i][1]
    next_goal_time = goal_info[i+1][0]
    team_score[goal_team] += 1 # 득접한 팀에 점수를 올려준다.

    if (team_score[1] != team_score[2]): # 승자 및 패자가 생겼으면 시간을 계산한다.
        if (team_score[1] > team_score[2]):
            winning_time[1] += (next_goal_time - goal_time)
        else:
            winning_time[2] += (next_goal_time - goal_time)
    latest_goal_time = goal_time

for i in range(1,len(winning_time)):
    m,s = winning_time[i] // 60 , winning_time[i] % 60
    print('{:0>2}:{:0>2}'.format(m,s))