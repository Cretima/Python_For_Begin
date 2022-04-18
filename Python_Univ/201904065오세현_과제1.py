name = str(input("이름: "))
problem = int(input("문제개수: "))
result = 0

print("*" * 35)

for problem in range (problem) :
    print("%d 번문제를해결했나요?(y/n):" %(problem + 1))
    c = str(input())
    if c == "y":
        result += 1
    else:
        result += 0

print("*" * 35)

print(name,"학생, 총", result,"문제를 해결했습니다.")
