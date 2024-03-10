n = int(input())
sellings = [input() for _ in range(n)]

# 책이 나타난 횟수를 값으로 가지고, key : 책제목
books = dict()
for book in sellings:
    if book in books.keys():
        books[book] += 1
    else :
        books[book] = 1
result = sorted(books.items(), key=lambda x : (-x[1], x[0]))[0][0] # 값 기준으로 정렬, 이름 사전순
print(result)



