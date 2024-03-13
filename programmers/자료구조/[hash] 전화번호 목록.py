"""
조건 : phone_book의 길이가 1,000,000이여서 O(N^2) 미만의 로직을 구성해야 한다.
idea : {key : 전화번호 ,value} 딕셔너리를 만들어서, 탐색 시 O(1) 복잡도로 가능하게 하여 이중for문O(N)을 소화한다.

🔴 해쉬는 key-value의 구조가 굳이 필요하지 않더라도, 탐색시 용이함 때문에 key만 내용이 유의하게 하여 list처럼 쓰는 경우도 있다.
해당 문제가 그런 케이스이다.
"""

def solution(phone_book):
    dictPB = dict()
    for phone in phone_book:
        dictPB[phone] = 1

    for number in phone_book:
        jd = ""
        for num in number:
            jd += num
            if (jd in dictPB) and jd != number :
                return False

    return True

print(solution(["123","456","789"]))