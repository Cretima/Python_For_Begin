# # 22.01.30
# # 함수, 전달값, 반환값, 기본값, 키워드값
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# def deposit(balance, money): # 입금
#     print(f"입금이 완료되었습니다. {balance + money} 원 입니다.")
#     return balance + money # return 해당 전달된 결과값을 반환한다

# def withdraw(balance, money): # 출금
#     if balance >= money: # 잔액이 출금보다 많으면
#         print(f"출금이 완료되었습니다. 잔액은 {balance - money}원 입니다")
#         return balance - money
#     else:
#         print(f"출금 오류, 잔액을 다시 확인해주세요. 잔액은 {balance}원 입니다")
#         return balance

# def withdraw_night(balance, money, commission = 100): # 저녁에 출금/ 커미션 기본값
#     print(f"수수료는 {commission}, 잔액은 {balance}원 입니다.")
#     return commission, balance - money - commission # 튜플 형식으로 두 값 반환

# balance = 0 #잔액
# balance = deposit(balance, 2000)
# balance = withdraw(balance, 3000)
# balance = withdraw(balance, 500)

# commission, balance = withdraw_night(balance, 500) # 커미션 값을 설정 안해도 기본값 설정으로 리턴 만약 커미션 값 설정하면 그 값으로 리턴됨.

# withdraw_night(commission = 200, money = 500, balance = 3000) # 키워드 값(순서 상관X)


# # 가변인자 
# 아래 예시처럼 서로 다른 갯수의 값을 하나의 함수로 사용할때 *____(넣고 싶은 만큼의 수를 변수를 만듬)

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print(f"이름 : {name}\t나이 : {age}\t", end = " ") # end=" " 다음줄 출력문을 출력할때, 이번 출력문 옆에 한칸 뛰고 이어서 출력
#     print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language):
    print(f"이름 : {name}\t나이 : {age}\t", end = " ") # end=" " 다음줄 출력문을 출력할때, 이번 출력문 옆에 한칸 뛰고 이어서 출력
    for lang in language:
        print(lang, end=" ")
    print() # 줄바꿈을 위한 공백 출력

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript") # 이름 : 유재석   나이 : 20        Python Java C C++ C# JavaScript
profile("김태호", 23, "Kotlin", "Swift") # 이름 : 김태호   나이 : 23        Kotlin Swift