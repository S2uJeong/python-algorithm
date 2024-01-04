def test(num):
    print("It is Test")
    return num**2

print(test(2))
print('\n')
test(2)
print('\n')
print('람다식 활용:')
def add(a,b):
    return a + b
print(add(3,7))

print((lambda a,b : a + b)(3,7))

