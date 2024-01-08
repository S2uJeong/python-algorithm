# 오답노트
## index 0 부터 시작하는거 잊지 않기
## sum() 함수는 변수로 iterable 형만 받는다.
## 딕셔너리형 value 기준으로 정렬하는 방법 : sorted(dict.items())
## key 기준으로 정렬 : sorted(dict) - key값만 정렬해나옴을 주의

# n,m = map(int,input().split())
def first_try(n,m):
    sum_dict = {}
    # 주사위로 나올 수 있는 경우의 수에 대한 합과 빈출횟수로 딕셔너리 자료형에 추가한다.
    for i in range(1,n+1):
        for j in range(1,m+1):
            tmp = sum([i,j])
            if tmp in sum_dict.keys():
                sum_dict[tmp] += 1
            else : sum_dict[tmp] = 1
    # 빈출횟수 기준으로 내림차순 정렬한 뒤, 제일 큰 수와 같은 것들만 result에 추가한다.
    sorted_list = sorted(sum_dict.items(), key= lambda x : -x[1])
    max = sorted_list[0][1]
    result = []
    for duo in sorted_list:
        if duo[1] < max :
            break
        else : result.append(duo[0])

    print(*result)

def example(n,m):
    cnt = [0]*(n+m+3) # +3은 그냥 넉넉히 넣어준다는 의미..
    max = -(1e8)
    for i in range(1,n+1):
        for j in range(1,m+1):
            cnt[i+j] += 1 # 딕셔너리가 아닌 리스트의 인덱스 값으로 표현하네. 근데 자료양이 많아지면 내 방식이 더 성능이 좋을 듯
    for i in range(n+m+1):
        if cnt[i] > max :
            max = cnt[i]
    for i,val in enumerate(cnt):
        if max == val:
            print(i, end=' ')

example(4,6)
