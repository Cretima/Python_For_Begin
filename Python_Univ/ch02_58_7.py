def Sum(x,y):
    global result
    result = x + y
    return result
    

a = int(input("숫자1 입력: "))
b = int(input("숫자2 입력: "))
result = 0

print(f"{a} + {b} = {Sum(a,b)}")

