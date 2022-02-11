'''
    끄적끄적
    아래 예제처럼 하나의 유닛(ex. tank)을 여러개(10개, 100개)를 만들때 일일히 코드를 쓰기 힘들기에
    class(객체를 만드는 틀(ex. 와플기계) 즉, 코드(재료)만 넣어주면 객체(와플)을 만들어줌.)를 사용
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
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f"{self.name} 유닛이 생성되었습니다.")
        print(f"체력 {self.hp}, 공격력 {self.damage}")

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 30)
