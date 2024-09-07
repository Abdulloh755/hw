
class SuperHero:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.fly = False

    def double_hp(self):
        self.hp *= 2

    def square_hp(self):
        self.hp **= 2
        self.fly = True

    def true_phrase(self):
        print("True in the True_phrase")


class AirHero(SuperHero):
    def __init__(self, name, hp, damage, altitude):
        super().__init__(name, hp, damage)
        self.altitude = altitude  # Добавляем собственное свойство altitude

    # Переопределение метода square_hp
    def square_hp(self):
        super().square_hp()
        print(f"Now {self.name} has hp {self.hp} and can fly: {self.fly}")


class EarthHero(SuperHero):
    def __init__(self, name, hp, damage, terrain):
        super().__init__(name, hp, damage)
        self.terrain = terrain

    def square_hp(self):
        super().square_hp()
        print(f"Now {self.name} has hp {self.hp} and can fly: {self.fly}")


class Villain(SuperHero):
    def __init__(self, name, hp, damage, villain_type):
        super().__init__(name, hp, damage)
        self.people = "monster"  # Изменяем значение атрибута people
        self.villain_type = villain_type

    def gen_x(self):
        pass

    def crit(self, other):
        if hasattr(other, 'damage'):
            print(f"Damage before crit: {other.damage}")
            other.damage **= 2
            print(f"Damage after crit: {other.damage}")


air_hero = AirHero(name="WindMaster", hp=100, damage=20, altitude=1000)
earth_hero = EarthHero(name="StoneGiant", hp=150, damage=30, terrain="mountain")

villain = Villain(name="DarkLord", hp=200, damage=50, villain_type="Sorcerer")

air_hero.square_hp()  # Увеличивает hp в квадрат и меняет fly на True
earth_hero.square_hp()  # Увеличивает hp в квадрат и меняет fly на True
air_hero.true_phrase()  # Выводит "True in the True_phrase"


villain.crit(air_hero)

print(f"{air_hero.name}'s damage: {air_hero.damage}")
print(f"{earth_hero.name}'s damage: {earth_hero.damage}")




