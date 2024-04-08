'''
page.314
화폐 단위를 기준으로 오름차순 정렬, 이후에 1부터 차례대로 특정한 금액을 만들 수 있는지 확인
'''
n = int(input())
moneys = list(map(int,input().split()))

def failed(moneys) :
    # 있는 동전 단위로 나올 수 있는 금액 다 구해서 list에 넣기
    # 동전의 개수는 1,000개가 최대 이므로 이중 for문 사용가능
    ways = []
    for i in range(len(moneys)):
        tmp_money = i
        ways.append(i)
        for j in range(len(moneys)):
            if i != j :
                tmp_money += moneys[j]
                ways.append(tmp_money)

    # set 자료구조로 중복제거
    set_ways = set(ways)
    print(set_ways)

    result = 0
    # 1 ~ 1,000,000 까지 ways에서 없는게 있다면 바로 return 하면 최소값이 된다.
    for i in range(1,1000001):
        if i not in list(set_ways):
            result = i
            return result


print(failed(moneys))

def solution(moneys):
    moneys.sort()

    target = 1
    for money in moneys:
        if target < money:
            return target
        target += money

print(solution(moneys))