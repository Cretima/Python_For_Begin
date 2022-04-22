# # 예외처리
# 1. try; 테스트할 실행문
# 2. except; 오류가 발생하면 호출됨.
# 3. else; 오류가 없으면 호출됨.


'''class MyError(Exception): # 방법 1
    pass'''

class MyError(Exception): # 방법 2
    def __str__(self):
        return "거짓말 하지 마세요."

def say_age(age):
    print("나이가 {0}입니까?".format(age))
    if age > 100:
        raise MyError() # 에러를 반환한다.
    
# main

try:
    age=int(input('나이를 입력하세요: '))
    say_age(age)

#except MyError: # 방법 1
    #print("거짓말 하지 마세요.")

except MyError as e: # 방법 2
    print(e)

except ValueError as e: # [발생오류 [as 오류메세지 변수]]
    print(e)
    print("숫자로만 알려주세요.")
else:
    if age <= 18:
        print('미성년자는 출입금지입니다.')
    else:
        print('환영합니다. 고객님')


        
