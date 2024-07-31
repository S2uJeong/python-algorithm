"""
N보다 작거나 같은 모든 소수 찾기
1. 가장 작은 수 pick -> 소수
2. 해당 수의 배수 다 지운다.
3. 남은 수가 있을때 까지 1~2 반복
"""
N,K = map(int, input().split())
nums_list = [1] * (N+1) # idx를 숫자로 이용할 것이기 때문에 (N+1)로 길이 설정 / val - 0 : 삭제됨, 1 : 아직 있음

for i in range(2,N+1):
    flag = False
    for j in range(i,N+1):
        if j % i == 0 and nums_list[j]:
            K -= 1
            nums_list[j] = 0

        if K <= 0 :
            print(j)
            flag = True
            break
    if flag :
        break