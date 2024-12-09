'''
가장 긴 짝수 연속한 부분 수열

- 홀수만을 제거해야 한다는 접근까지는 맞았음
- 삭제를 어느 규칙으로 하면서 수열의 길이를 구해야 할지 고민 과정이 어려웠음

" K를 기준으로 수를 맞출 수 있게 left, right를 조절하며 수열을 표시해준다. 그리고 매번 최대 길이를 계산한다."
1. 홀수의 개수를 기준으로 K개를 넘는지 분기
2-1. 홀수 > K : left를 오른쪽으로 조정
2-2. 홀수 <= K : right를 오른쪽으로 조정
3. 매 턴 마다 max 값을 계산한다.
'''

N,K = map(int,input().split())
nums = list(map(int,input().split()))

left = 0
right = 0
max_length = 0
odd_cnt = 0
even_cnt = 0
while(right < N):
    if odd_cnt <= K :
        if nums[right] % 2 :
            odd_cnt += 1
        else :
            even_cnt += 1
        right += 1
    else :
        if nums[left] % 2 :
            odd_cnt -= 1
        else:
            even_cnt -= 1
        left += 1

    if even_cnt > max_length:
        max_length = even_cnt


print(max_length)