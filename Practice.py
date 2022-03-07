'''
pass : 메소드를 만들고 그 안에 pass를 넣으면 일단 넘어가게 됨
참조 : 맨 밑에 줄
--> continue와 비슷한건가?? --> 컨티뉴와 다르게 그 줄만 넘어가고 계속 실행됨.
'''
# 일반유닛
class Unit:
    def __init__(self, name, hp, speed):
        # __init__ : class를 쓸때 자동으로 붙는 호풀되는 함수
        self.name = name 
        self.hp = hp
        self.speed = speed
        print(f"{name} 유닛이 생성되었습니다.")

    # 지상 유닛 이동 메소드
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))

    # 공격 받음 메소드 
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage # 받은데미지를 빼서 남아있는 체력 수식
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))
        
# 공격유닛
class AttackUnit(Unit): # AttackUni이 Unit을 상속받음
    def __init__(self, name, hp, speed, damage): # self는 자기자신을 뜻하며 class 내에선 앞에 무조건 써야함
        # __init__ : class를 쓸때 자동으로 붙는 생성자
        # self.name = name
        # self.hp = hp
        Unit.__init__(self, name, hp, speed) # 유닛을 통해 이름과 체력을 상속받음
                                      # 상속 받고 싶을땐 해당 class + . + 생성자 이름(def)
        self.damage = damage
    # 공격 메소드
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
        .format(self.name, location, self.damage))

class Marine(AttackUnit):
    def __init__(self):
        super().__init__("마린", 40, 1, 5)

    # 스팀팩 : 일정시간동안 이동 및 공격속도 증가, 체력 10 감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다 (hp 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))


# 탱크
class Tank(AttackUnit):
    # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능, 이동 불가.
    seize_developed = False # 시즈모드 개발여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return

        # 현재 시즈모드가 아닐때 -> 시즈모드
        if self.set_seize_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True

        # 현재 시즈모드일 때 -> 시즈모드 해제
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode =  False


# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    # 공중 유닛 이동
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable): # 다중상속
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed는 0으로
        Flyable.__init__(self, flying_speed)

    # 지상 이동도 move임으로 구분하기 귀찮으니 통일한 같은 이름의 메소드
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False # 클로킹 모드 (해제 상태)

    def clocking(self):
        if self.clocked == True: # 클로킹 모드 -> 모드 해제
            print("{0} : 클로킹 모드 해제합니다.".format(self.name))
            self.clocked = False
        else: # 클로킹 모드 해제 -> 모드 설정
            print("{0} : 클로킹 모드 설정합니다.".format(self.name))
            self.clocked = True





