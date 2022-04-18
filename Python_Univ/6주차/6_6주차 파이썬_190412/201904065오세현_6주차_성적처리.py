e = int(input("영어 점수 입력 :"))
m = int(input("수학 점수 입력 :"))
result = e + m

if result >= 110:
    if e >= 40:
        if m >+ 40:
            print("합격")
        else :
            print("불합격 : 수학부족")
    else :
        print("불합격 : 영어부족")
else:
    print("불합격 : 총합부족")
    
