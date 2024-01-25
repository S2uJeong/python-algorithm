def 전위순회(v):
    # 이 방법을 많이 쓴다.
    if v > 7:
        return
    else :
        print(v,end=' ')
        전위순회(v*2)
        전위순회(v*2+1)

def 중위순회(v):
    if v > 7:
        return
    else:
        중위순회(v * 2)
        print(v, end=' ')
        중위순회(v * 2 + 1)


def 후위순회(v):
    # 병합정렬에서 많이 쓰인다.
    if v > 7:
        return
    else:
        후위순회(v * 2)
        후위순회(v * 2 + 1)
        print(v, end=' ')

전위순회(1)
print()
중위순회(1)
print()
후위순회(1)