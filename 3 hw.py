
class Flying:
    def fly(self):
        self.state = "в воздухе"
        print("Амфибия летает. Состояние: ", self.state)


class Swimming:
    def swim(self):
        self.state = "в воде"
        print("Амфибия плывет. Состояние: ", self.state)


class Amphibian(Flying, Swimming):
    def __init__(self):
        self.state = "на земле"
        print("Амфибия создана. Состояние: ", self.state)

    def land(self):
        self.state = "на земле"
        print("Амфибия на земле. Состояние: ", self.state)

    def get_state(self):
        print("Текущее состояние амфибии: ", self.state)


amphibian = Amphibian()

amphibian.fly()  #
amphibian.get_state()

amphibian.land()
amphibian.get_state()

amphibian.swim()
amphibian.get_state()

amphibian.land()
amphibian.get_state()