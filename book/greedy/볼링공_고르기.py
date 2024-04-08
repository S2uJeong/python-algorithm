'''
1. 두 사람은 서로 무게가 다른 것을 골라야 함.
2. 여러 조합 중 조건을 만족하는 경우의 수 출력
제약
1. 볼링공의 개수 1~1,000 -> O(N^2)
'''
n,m = map(int,(input().split()))
balls = list(map(int,(input().split())))
def first_solution(balls):
    result = 0

    for i in range(len(balls)):
        for j in range(len(balls)):
            if i != j :
                if balls[i] != balls[j]:
                    result += 1

    return result//2

print(first_solution(balls))

def second_solution(balls):
    result = 0

    for i in range(len(balls)):
        for j in range(i+1,len(balls)):
            if balls[i] != balls[j]:
                result += 1
    return result

print(second_solution(balls))

'''
공의 무게를 메모한 list를 활용하여 이중 for문을 사용 안 하고 풀이
중복 선택 하지 않게 n 변수를 활용해서 경우의 수를 구함
'''
def third_solution(balls,m):
    # 볼링공의 무게 범위는 1~10이다.
    array = [0] * 11
    for i in balls:
        array[i] += 1
    result = 0
    n = len(balls)
    for i in range(1,m+1): # m : 문제에서 제시된 공의 최대 무게
        n -= array[i] # 무게가 i인 볼링공의 개수 (A가 선택할 수 있는 개수) 제외 (어차피 같은 무게의 볼링공은 선택 불가하므로)
        result += array[i] * n # B가 선택하는 경우의 수와 곱한다.

print(third_solution(balls,m))