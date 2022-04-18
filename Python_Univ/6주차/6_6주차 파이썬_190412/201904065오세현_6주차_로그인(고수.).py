아이디 = input("ID:")
비번 = input("PW:")
계정id = "test"
계정pw = "1234"
if 아이디 == 계정id and 비번 == 계정pw :
    print("로그인 성공")
elif 아이디 != 계정id:
    print("로그인 실패 : ID 틀렸음")
elif 비번 != 계정id:
    print("로그인 실패 : PW 틀렸음")
else:
    print("잘못 입력하셨습니다.")
