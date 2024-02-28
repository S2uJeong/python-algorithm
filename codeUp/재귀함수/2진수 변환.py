"""
실패한 코드
n = 0 으로 들어오면 버그
"""
def fail(n):
    if n == 1 :
        print(1, end='')
        return
    fail(n//2)
    print(n % 2, end='')


def f(n):
    if n <= 0 :
        return '0'
    elif n == 1 :
        return '1'
    if n % 2 == 0 :
        return f(n//2) + '0'
    elif n % 2  == 1 :
        return f(n//2) + '1'


print(f(int(input())))