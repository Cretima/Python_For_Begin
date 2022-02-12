'''
    끄적끄적
    아래 예제처럼 하나의 유닛(ex. tank)을 여러개(10개, 100개)를 만들때 일일히 코드를 쓰기 힘들기에
    class(객체를 만드는 틀(ex. 와플기계) 즉, 코드(재료)만 넣어주면 객체(와플)을 만들어줌.)를 사용
    self는 멤버 변수()라 지칭 - class 내의 변수 but 전역변수처럼 외부에서 사용가능.
'''

# # class(클래스) 서로 연관이 있는 변수와 함수의 집합(객체 틀)


# # 아래 주석 코드는 상황 설명을 위한 예제

# # 마린 : 공격 유닛, 군인 ,총을 사용
# name = "마린" # 유닛 이름
# hp = 50 # 체력
# damage = 5 # 공격력

# print(f"{name} 유닛이 생성되었습니다.")
# print(f"(채력 {hp}, 공격력 {damage} \n")

# # 탱크 : 공격 유닛, 포를 이용한 원거리 공격, 일반 모드, 시즈 모드(장거리)
# tank_name = "탱크"
# tank_hp = 200
# tank_damage = 30

# print(f"{tank_name} 유닛이 생성되었습니다.")
# print(f"(채력 {tank_hp}, 공격력 {tank_damage} \n")

# # 탱크2 : 공격 유닛, 포를 이용한 원거리 공격, 일반 모드, 시즈 모드(장거리)
# tank2_name = "탱크"
# tank2_hp = 200
# tank2_damage = 30

# print(f"{tank2_name} 유닛이 생성되었습니다.")
# print(f"(채력 {tank2_hp}, 공격력 {tank2_damage} \n")


# def attack(name, location, damage): # 유닛이 공격갈때
#     print(f"{name} : {location} 방향으로 적군을 공격합니다. [공격력 {damage}]")

# # main
# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank2_damage)


class Unit:
    def __init__(self, name, hp, damage):
        # __init__ : class를 쓸때 자동으로 붙는 호풀되는 함수
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f"{self.name} 유닛이 생성되었습니다.")
        print(f"체력 {self.hp}, 공격력 {self.damage}")

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 30)
# tank2 = Unit("탱크", 30) # self 제외, __init__ 값이 지정되지 않으면 오류가 발생

# # 멤버 변수 사용 예
# 레이스 : 공중유닛, 비행기, 클로킹(스텔스)
wraith1 = Unit("레이스", 80, 5)
print(f"유닛 이름 : {wraith1.name}, 공격력 : {wraith1.damage}")

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만듬
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True # class에 없는 것을 외부에서 만들수있음 but wraith1 같은 경우엔 사용 불가.

if wraith2.clocking == True: 
    print(f"{wraith2.name}는 현재 클로킹 중입니다.")