i = input("ID:")
p = input("PW")

if i == "test" and p == "1234" :
    print("로그인 성공")
else:
    if i != "test" and p != "1234":
        print("로그인 전체 틀렸음")
    elif i != "test":
        print("로그인 실패 : ID 틀렸음")
    else :
        print("로그인 실패 : PW 틀렸음")
        
     
    
