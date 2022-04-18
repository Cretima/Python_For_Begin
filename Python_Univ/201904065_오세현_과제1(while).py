name = str(input("이름: ")) #이름 입력
problem = int(input("문제개수: ")) #문재개수 입력
result = 0 #결과값 0초기화 (문자를 숫자로 변환)
n = 1 #반복횟수, 0초기화

print("*" * 35)

while n < (problem + 1) : #문제 전 개수까지 반복
    print(f"{n}번문제를해결했나요?(y/n):") # 몇 번 문제인지 출력
    c = str(input()) # y or n 입력
    if (c == "y") or (c == "Y"):
        n += 1
        result += 1 # 만약 y면 숫자로 결과값에 +1
    elif (c == "n") or (c == "N"):
        n += 1
        result += 0 # y가 아니면 결과값 그대로
    else: # 둘다 아니면 재입력 안내문 출력후 다시 시도.
        print("잘못 입력하셨습니다 다시 입력하세요.\n", "*"*35, "\n")


print("*" * 35)

print(fr"{name} 학생, 총, \"{result}\" 문제를 해결했습니다.") #위의 반복문 이름 및 최종 결과값 출력
# or print(f"{name} 학생, 총 {result}문제를 해결햇습니다."
"/    r   f'{ }'  fr'{}'    /"

