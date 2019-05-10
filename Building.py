from PyQt5.QtWidgets import QLabel

UPGRADE = 1000
LAND = 2000
LEVEL1 = 3000
LEVEL2 = 4000
ORIGINAL_CASH = 10000

class Building(QLabel):

    def __init__(self, *args):
        super(Building, self).__init__(*args)
        self.owner = None
        self.level = 0
        self.color_suit = []

    def set_owner(self, owner, color):
        self.owner = owner
        self.color_suit = color
        self.setStyleSheet(self.color_suit[self.level])

    def upgrade(self):
        if self.level <= 1:
            self.level += 1
            self.setStyleSheet(self.color_suit[self.level])


class Player(QLabel):

    def __init__(self, *args):
        super(Player, self).__init__(*args)
        self.name = None
        self.cash = ORIGINAL_CASH
        self.color_suit = None
        self.land = 0
        self.level1_house = 0
        self.level2_house = 0

    def set_name(self, name):
        self.name = name

    def get_money(self):
        money = self.level1_house * LEVEL1 + self.level2_house * LEVEL2 + self.land * LAND + self.cash
        return money

    def get_house(self):
        house = self.land + self.level1_house + self.level2_house
        return house

    def initiate_color(self, suit):
        if suit == 1:
            self.color_suit = ["background-color: rgb(255, 222, 99);"
                , "background-color: rgb(239, 151, 25);"
                , "background-color: rgb(237, 105, 66);"]
        elif suit == 2:
            self.color_suit = ["background-color: rgb(150, 218, 241);"
                , "background-color: rgb(0, 184, 238);"
                , "background-color: rgb(84, 111, 180);"]
        else:
            raise ValueError('Unknown color suit')

    def buy_building(self, building):
        assert isinstance(building, Building)
        # print(building.owner, self.name)
        if building.owner is None:
            if self.cash >= LAND:
                self.cash -= LAND
            else:
                raise ValueError("No enough money.")
            building.set_owner(self.name, self.color_suit)
            self.land += 1
        elif building.owner == self.name:
            if self.cash >= UPGRADE:
                self.cash -= UPGRADE
            else:
                raise ValueError("No enough money.")
            if building.level == 0:
                self.land -= 1
                self.level1_house += 1
            elif building.level == 1:
                self.level2_house += 1
                self.level1_house -= 1
            building.upgrade()
        else:
            raise ValueError("Not owner of the building, cannot upgrade.")

    def fine_money(self, level):
        if level == 0:
            m = 0
        elif level == 1:
            m = 1000
        elif level == 2:
            m = 2000
        self.cash -= m
        return m

