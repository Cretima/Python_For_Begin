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

    # 지상 유닛 이동 메소드
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))
        
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
    # 공격 받음 메소드
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage # 받은데미지를 빼서 남아있는 체력 수식
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


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


# Pass 부분
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass # 일단 넘어가!
        Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0)
        self.location = location


