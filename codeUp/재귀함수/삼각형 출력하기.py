def recur(n) :
    if n == 1:
        print("*")
        return

    recur(n-1)
    print("*" * n)

recur(int(input()))