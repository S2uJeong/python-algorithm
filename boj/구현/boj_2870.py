"""
각 글자를 for문으로
 - char 단위로 for문 돌린다. 100 * 100
 - 숫자가 시작되면 string에 해당 문자를 쭉 모은다.
 - 모든 숫자 문자는 숫자로 변환하야 한 list에 모은다.
"""

T = int(input().rstrip())
numbers = []
for _ in range(T):
    input_string = input().rstrip()
    number_string = ""
    for c in input_string:
        if ord(c) < 65: # 숫자임
            number_string += c
        else:
            if number_string :
                numbers.append(int(number_string))
                number_string = ""

    if number_string:
        numbers.append(int(number_string))

numbers.sort()
for n in numbers:
    print(n)

