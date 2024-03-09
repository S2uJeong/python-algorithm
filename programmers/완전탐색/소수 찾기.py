"""
https://school.programmers.co.kr/learn/courses/30/lessons/42839

1. 리스트 + 연산 : 리스트 두개 합치기를 사용함으로써 구현의 어려움이 풀림.
2. join - "".join(['가','나','다']) -> "가나다"
3. 소수 판별하기 함수
"""
from itertools import permutations

def solution(numbers):
    nums = set(trans_num(numbers))
    answer = 0
    for val in nums:
        if is_prime(val) == True :
            answer += 1
    return answer

def trans_num(numbers):
    nums = [n for n in numbers]
    permu = []
    for i in range(1, len(numbers) + 1):
        permu += list(permutations(nums, i))
    #print(permu)
    nums = [int(("").join(p)) for p in permu]
    return nums

def is_prime(num):
    if num < 2 :
        return False
    for i in range(2,num):
        if num % i == 0 :
            return False
    return True

print(solution("17"))