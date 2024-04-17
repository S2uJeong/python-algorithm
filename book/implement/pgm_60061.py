"""
1. 설치/삭제 구분
    1-1 설치 : 설치할 대상의 위치가 올바른지 확인하는 주변탐색
    1-2 삭제 : 삭제시, 조건과 안 맞는게 생기는지 전체 탐색
2. 기둥/보 구분
    2-1 기둥 : 좌표 기준 위쪽 / 바닥 위, 보의 한쪽 끝 위, 또 다른 기둥위
    2-2 보 : 좌표 기준 오른쪽 / 한쪽 끝 부분이 기둥 위, 양쪽 끝 부분이 다른 보와 연결
- 아이디어
    - 나는 build로 들어오는 좌표에 대해서 유효성 검증을 하려고 했는데,
    - answer 리스트 자료구조를 이용하여 가능한 건축물의 정보를 담아놓고, 설치/삭제마다 해당 리스트를 다 탐색하는 방법을 이용해서 풀 수 있음
        - 삭제 시, answer.remove()
        - 설치 시, answer.append()
        - 그리고 반영한 상태의 answer에 대해 유효성 검증을 진행하고, 틀릴 시 작업을 다시 append()/remove()하여 원상복귀 한다.
"""
def solution(n, build_frame):
    answer = [[]]
    return answer

"""
구조물에 대한 유효성 검증 함수 
    return {True : 설치/삭제 가능}, {False : 설치/삭제 불가능} 
    설치든, 삭제든 모든 영역의 구조물이 조건을 만족해야 한단것을 전제로 검증 
"""
def possible(answer): # answer = [[x,y,a],...,]
    for x,y,a in answer:
        # 기둥인지 보인지
        if a == 0 : # 기둥
            if y == 0 or [x-1, y, 1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
                continue
            else:
                return False
        elif a == 1 : # 보
            if [x, y-1 ,0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            else:
                return False
    return True


def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x,y,a,b = frame
        if b == 0 : # 삭제하는 경우
            answer.remove([x,y,a])
            if not possible(answer):
                answer.append([x,y,a])
        if b == 1 :
            answer.append([x,y,a])
            if not possible(answer):
                answer.remove([x,y,a])
    return sorted(answer)