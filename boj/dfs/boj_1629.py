# O(logB)
def exp(a,b,c):
    result = 1
    a = a % c
    while b > 0 :
        if b % 2 == 1:
            result = (result * a) % c
        b = b // 2
        a = (a*a) % c
    return result

# 분할 정복, O(logB) : B를 2로 나누어가며 작은 부분 문제로 쪼갠다.
    # B가 짝수일 경우: A^B = (A^(B//2))^2
    # B가 홀수일 경우: A^B = A * (A^(B//2))^2
def divide_conquer(a,b,c):
    if b == 1 :
        return a % c
    if b % 2 :
        return (divide_conquer(a,b//2,c)**2*a) % c
    else:
        return (divide_conquer(a,b//2,c)**2) % c

A,B,C = map(int,input().split())
print(divide_conquer(A,B,C))
