total = 0
a = int(input("숫자를 입력:"))

for b in range(1, a+1, 1):
    total += b

print("1부터 %d까지의 합:"%a, total)
