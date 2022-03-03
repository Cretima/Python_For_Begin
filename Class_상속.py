'''
메소드 : __init__ 이 아닌 나머지 def something을 가르킴
상속 : ex) 일반유닛과 공격유닛에 self.name, hp가 겹침으로 
상속(Unit -> AttackUnit)을 통해 빌려 가져다쓴다
다중상속 여러 부모 클래스를 상속받음(공중유닛 부분)
'''
# 일반유닛
class Unit:
    def __init__(self, name, hp):
        # __init__ : class를 쓸때 자동으로 붙는 호풀되는 함수
        self.name = name 
        self.hp = hp
        
# 공격유닛
class AttackUnit(Unit): # AttackUni이 Unit을 상속받음
    def __init__(self, name, hp, damage): # self는 자기자신을 뜻하며 class 내에선 앞에 무조건 써야함
        # __init__ : class를 쓸때 자동으로 붙는 생성자
        # self.name = name
        # self.hp = hp
        Unit.__init__(self, name, hp) # 유닛을 통해 이름과 체력을 상속받음
                                      # 상속 받고 싶을땐 해당 class + . + 생성자 이름(def)
        self.damage = damage
    # 공격
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
        .format(self.name, location, self.damage))
    # 공격 받음
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

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable): # 다중상속
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)
        
# main

valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")