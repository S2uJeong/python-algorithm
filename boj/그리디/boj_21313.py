"""
사전순으로 제일 앞서는 수열을 만드려면 1-2 의 수열의 반복하는것 만큼이 결국 정답이 된다.
문어 : 4 ~ 1000
문어 4 : 1-2-1-2
문어 5 : 1-2-1-2-3
문어 6 : 1-2-1-2-1-2

규칙 : 문어가 짝수면, 1 2 * 2
            홀수면, 1 2 * 2 , 3
"""

N = int(input())
answer = [1,2]
if N % 2 == 0 :
    for i in range(N):
        print(answer[i%2], end=' ')
else :
    for i in range(N-1):
        print(answer[i%2], end=' ')
    print('3', end='')