class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.health_points = health_points
        self.catchphrase = catchphrase

    def indroduce(self):
        return (f"Меня зовут"
                f"{self.name},мое прозвище"
                f"{self.nickname}. Моя супер сила"
                f"{self.superpower}!")

    def say_catchphrase(self):
        return f"Моя коронная фраза:{self.catchphrase}"

    def check_catchphrase(self):
        return f"у меня {self.health_points}очков здоровье."


hero = SuperHero("Петр", "Супермен", "Летать", 100, "Я спасу мир!")

print(hero.indroduce())
print(hero.say_catchphrase())
print(hero.check_health())
