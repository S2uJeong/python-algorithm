def digit_sum(p_num):
    sum = 0
    while p_num > 0 :
        sum += p_num % 10
        p_num = p_num // 10
    return sum

print("자릿수를 더해볼 숫자를 입력해주세요")
in_num = int(input())
print(digit_sum(in_num))