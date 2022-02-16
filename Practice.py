a = 35
b = 60
c = 4
num1 = 96.3
num2 = 88.325

num3 = int(input("상수 입력: "))

result = (a + b - c) * num1 % 88.325 * 3

print(f"{result}"\n)

print(f"실제 결과는 이거야 {result % num3}")
