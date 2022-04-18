## 함수선언 부분 ##
def myFunc():
    print("함수를 호출함")


##전역변수 선언##
gVar = 100


##메인 코드 부분##
if __name__ == '__main__' : # C언어 처럼 메인함수 효과 만들어줌.
    print("메인함수 부분이 실행됩니다.")
    myFunc()
    print(f"전역변수 값: {gVar}")
