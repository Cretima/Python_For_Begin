아이디 = input("ID:")
비번 = input("PW:")
if 아이디 == "test":
    if 비번 == "1234":
        print("로그인 성공")
    else:
        print("로그인 실패 : 비번")
else :
    print("로그인 실패 : ID")
