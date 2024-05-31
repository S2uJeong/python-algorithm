"""
- string 길이가 홀수냐/짝수냐에 따라 기준이 달라져 가운데 기점으로 양쪽을 비교하는게 쉽지 않았다.
- 하지만 문제 그대로 단순하게 탐색하면서 i부분과 뒷 부분이 같아지는 지점을 찾아 탐색해온 idx만큼 더해준다는 방법이 유용
"""

#def check(string,n):
#   while n <= len(string) - n:
#       if string[n] != string[len-n]:
#           return False
#   return True

data = input()
for i in range(len(data)):
    if data[i:] == data[i:][::-1]:
        print(len(data) + i)
        break