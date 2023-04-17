# 숫자(numbers)

a = 2
b = 3

print(a + b) # 더하기
print(a - b) # 빼기
print(a * b) # 곱하기
print(a / b) # 나누기
print()

print(a ** b) # a의 b제곱

print((a + b) * b)
print()

print(a // b) # 몫
print(a % b)  # 나머지
print()


# 실수(Float) - 십진 부동 소수점

x = 10.0
y = 0.3
z = 1

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print()

print(x + z)
print(x - z)
print(x * z)
print(x / z)
print()

# 실수와 연산하는 수는 그 결과가 모두 실수이다.


price = 12_349_000_000_000
print(price) # _로 해도 값은 같음 구분하기 좋은 역할
print()


# 상수(constants) - 대문자
PI = 3.141592
print(PI)
print()


# 문자열-숫자 간 변환

c = 100
d = "100"
e = "0.453"

c = str(c)
d = int(d)
e = float(e)