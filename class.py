result = 0
def add(num):
    global result
    result += num
    return result
print(add(3))
print(add(4))

result1 = 0
result2 = 0
def add1(num):
    global result1
    result1 += num
    return result1

def add2(num):
    global result2
    result2 += num
    return result2

print(add(3))
print(add(4))

print(add1(3))
print(add1(4))

print(add2(3))
print(add2(4))

# Class는 첫번째 글자를 대문자로 쓰는 것이 정석
# 함수, 조건, 반복문은 끝에 ' : '

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 =Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))
