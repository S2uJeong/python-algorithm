"""  투포인터
1. 글자가 회문인지 확인 해서 맞으면 바로 return 0  break
2. 글자를 제외 했을 때 회문이 되는지 확인해서, 맞으면 return 1  break
3. 나머지는 return 2   break

deque 활용하다가 코드 복잡해져서 투포인터로 변환, deque로 생각드는거 투포인트로 먼저 생각해보는게 좋을 듯
"""
def is_palindrome(string, left, right):
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True

def solution():
    left = 0
    right = len(in_str) - 1

    while left < right:
        if in_str[left] != in_str[right]:
            if is_palindrome(in_str, left+1, right) or is_palindrome(in_str, left, right-1):
                return 1
            else:
                return 2
        left += 1
        right -= 1

    return 0

T = int(input())
for _ in range(T):
    in_str = input()
    print(solution())
