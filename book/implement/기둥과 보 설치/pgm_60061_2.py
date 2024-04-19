def possible(answers):
    for answer in answers:
        x,y,a = answer
        if a == 0: # 구조물이 기둥일 때
            if y == 0 or [x-1,y,1] in answers or [x,y,1] in answers or [x,y-1,0] in answers : # 조건에 해당함
                continue
            else :
                return False
        else: # 구조물이 보일 때
            if [x,y-1,0] in answers or [x+1,y-1,0] in answers or ([x-1,y,1] in answers and [x+1,y,1] in answers):
                continue
            else :
                return False
    return True
def solution(n, build_frame):
    answer = []
    for bf in build_frame:
        x,y,a,b = bf
        if b == 1: # 설치
            answer.append([x,y,a])
            if possible(answer) == False :
                answer.pop()
        else : # 철수
            answer.remove([x,y,a])
            if possible(answer) == False :
                answer.append([x,y,a])

    answer.sort()
    return answer

n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
print(solution(n,build_frame))