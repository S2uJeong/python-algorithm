# ========= 이진 탐색 ==========
def solution_이진(n): # n = 가게 재고 부품 종류의 수
    import recursive_binary_search

    items = list(map(int,input().split())) # 가게 재고
    items.sort()
    m = int(input()) # 손님이 찾는 아이템 종류 수
    find_items = list(map(int,input().split())) # 손님이 찾는 재고

    for i in find_items:
        result = recursive_binary_search.binary_search(items,i,0,n-1)
        if result != None:
            print('yes', end=' ')
        else:
            print('no', end=' ')

# ======= 계수 정렬 ==========
def solution_계수정렬(n): # n = 가게 재고 부품 종류의 수
    items = [0] * 1000001

    # 전체 재고 부품 번호 입력 받아 기록 ✨✨✨
    for i in input().split():
        items[int(i)] = 1

    m = int(input())
    find_items = list(map(int,input().split()))

    # 손님이 요청한 부품이 있는지 확인
    for i in find_items:
        if items[i] == 1:
            print('yes', end=' ')
        else:
            print('no', end=' ')


# ======= 집합 자료구조 활용 ========
def solution_집합(n): # n = 가게 재고 부품 종류의 수
    items = set(map(int, input().split()))

    m = int(input())
    find_items = list(map(int,input().split()))

    for i in find_items:
        if i in items:
            print('yes', end=' ')
        else:
            print('no', end=' ')