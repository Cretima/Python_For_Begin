'''
끄적끄적
pass : 이름 그대로 일단 넘어가! (해당 줄을 넘기고 다음 줄로 간다.)
super() : 코드 밑줄 참조
'''

class Unit:
    def __init__(self):
        print("Unit 생성자")
    
    def something1(self):
        pass

    def something2(self):
        pass
        print("something")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")



class FlyableUnit_1(Flyable, Unit):
    def __init__(self):
        super().__init__()

class FlyableUnit_2(Unit, Flyable):
    def __init__(self):
        super().__init__()

# main

'''
아래 출력을 통해 super()는 "class FlyableUnit_2( {1}, {2} )"에서
맨 처음에있는 class( {1} )를 불러온다는것을 알 수 있다.
'''
dropship_1 = FlyableUnit_1() # 출력: Flyable 생성자
dropship_1 = FlyableUnit_2() # 출력: Unit 생성자

dropship_1.something1() # 오류가 나지 않고 pass로 인해 그냥 넘김.
dropship_1.something2() # 출력 : something
