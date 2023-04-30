print("안녕하세요")

greeting = "안녕하세요"
print(greeting)

greeting = "반갑습니다"
print(greeting)

my_greeting = "안녕하세요"
greeting_1 = "안녕"

city = "seoul"
print(city)

city.upper()
print(city.upper())

city = city.upper()
print(city)

city.lower()
print(city.lower())

city = city.lower()
print(city)

occupation = "developer     "
print(occupation)

occupation.rstrip()
print(occupation.rstrip())

occupation.lstrip()
occupation.strip()

print("INFP\nENFP\nISTJ\nESTJ")
print("INFP\tENFP\tISTJ\tESTJ")

score = "점수:90"
print(score.removeprefix("점수:"))

score_2 = "75점"
print(score_2.removesuffix("점"))

city = "서울 중구"
print(city.replace("서울", "서울시"))

si_1 = "용인"
gu_1 = "기흥"
address_1 = f"{si_1}시 {gu_1}구"
print(address_1)

si_2 = "서울"
gu_2 = "종로"
print(f"{si_1}시 {gu_1}구")
print(f"{si_2}시 {gu_2}구")

a = 2
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** b)
print(a + b * b)
print(a // b)
print(a % b)

x = 0.6
y = 0.3
z = 1
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x + z)
print(x - z)
print(x * z)
print(x / z)

price = 12_349_000_000_000
print(price)

PI = 3.141592
PI = 1.23
print(PI)

a = 100
b = "100"
c = "0.453"
a = str(a)
b = int(b)
c = float(c)

print(3 > 2)
print(3 == 3)
print(3 == 3.0)
print(3 is 3.0)

input("설치를 계속 진행하시겠습니까? (y/n): ")
text = input("출력할 텍스트를 입력해주세요: ")
print(text)

# 한 줄 주석
"""
여러 줄 주석입니다.
여러 줄 주석입니다.
여러 줄 주석입니다.
"""