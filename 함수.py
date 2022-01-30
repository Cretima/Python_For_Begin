# 22.01.30
# 함수, 전달값, 반환값, 기본값, 키워드값
def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money): # 입금
    print(f"입금이 완료되었습니다. {balance + money} 원 입니다.")
    return balance + money

def withdraw(balance, money): # 출금
    if balance >= money: # 잔액이 출금보다 많으면
        print(f"출금이 완료되었습니다. 잔액은 {balance - money}원 입니다")
        return balance - money
    else:
        print(f"출금 오류, 잔액을 다시 확인해주세요. 잔액은 {balance}원 입니다")
        return balance

def withdraw_night(balance, money, commission = 100): # 저녁에 출금/ 커미션 기본값
    print(f"수수료는 {commission}, 잔액은 {balance}원 입니다.")
    return commission, balance - money - commission # 튜플 형식으로 두 값 반환

balance = 0 #잔액
balance = deposit(balance, 2000)
balance = withdraw(balance, 3000)
balance = withdraw(balance, 500)

commission, balance = withdraw_night(balance, 500) # 커미션 값을 설정 안해도 기본값 설정으로 리턴 만약 커미션 값 설정하면 그 값으로 리턴됨.

withdraw_night(commission = 200, money = 500, balance = 3000) # 키워드 값(순서 상관X)