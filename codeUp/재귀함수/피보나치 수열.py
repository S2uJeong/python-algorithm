import sys
sys.setrecursionlimit(100000)

def f(n):
    if n <= 2 :
        return 1
    else :
        return f(n-2) + f(n-1)

print(f(int(input())))
