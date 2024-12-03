def makeIntArray():
    arr = list(map(int, input().split()))
    return arr

def makeStrArray():
    arr = list(input().split())
    return arr

def make2dArray(r):
    arr = [list(map(int,input().split())) for _ in range(r)]
    return arr

# 1924 -> [1,9,2,4]
def makeArrayFromNumber(num):
    arr = list(map(int,input()))
    return arr

array = make2dArray(4)
for arr in array:
    print(arr)