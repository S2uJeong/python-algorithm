"""
- 소수인지 아닌지 판별하는 함수
- 주어진 값부터 시작해서 소수면 바로 return, print
"""
def is_prime(num):
    if num <= 1 :
        return False
    for x in range(2,int(num ** 0.5)+1):
        if num % x == 0:
            return False
    return True

def print_smallest_prime_after_num(num):
    while True :
        if is_prime(num):
            print(num)
            return

        num += 1

T = int(input())
for _ in range(T):
    n = int(input())
    print_smallest_prime_after_num(n)