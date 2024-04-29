"""
안테나는 집이 설치된 좌표의 평균 값에 근처할 수록 각 집마다의 거리를 합한 값이 최고일 것이다.
"""
N = int(input())
houses = list(map(int, input().split()))
houses.sort()

# 중간값 출력
print(houses[(N-1)//2])
