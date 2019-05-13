from PyQt5.QtWidgets import QLabel

UPGRADE = 1000
LAND = 8000
LEVEL1 = 4000
LEVEL2 = 6000
ORIGINAL_CASH = 100000


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
        self.count = 0
        self.land = 0
        self.level1_house = 0
        self.level2_house = 0
        self.loaned_money = 0
        self.pay_back_time_remaining = 0
        self.pay_back_time_total = 0

    def set_name(self, name):
        self.name = name

    def get_money(self):
        money = self.level1_house * LEVEL1 + self.level2_house * LEVEL2 + self.land * LAND + self.cash
        return int(money)

    def get_house(self):
        house = self.land + self.level1_house + self.level2_house
        return house

    def get_max_loan(self):
        max_loan = 0.6 * self.get_money()
        return int(max_loan)

    def loan_money(self, loan):
        self.loaned_money += loan
        self.pay_back_time_total += 1
        self.pay_back_time_remaining = 1

    def money_to_pay(self):
        return (self.loaned_money * (1.1 ** self.pay_back_time_total) // 1000) * 1000

    def pay_debt(self):
        print("pay debt")
        if self.loaned_money != 0:
            if self.pay_back_time_remaining > 1:
                self.pay_back_time_remaining -= 1
            else:
                money_to_pay = self.money_to_pay()
                if self.cash >= money_to_pay:
                    self.cash -= money_to_pay
                    self.pay_back_time_total = 0
                    self.pay_back_time_remaining = 0
                    self.loaned_money = 0
                    return True
                else:
                    self.pay_back_time_total += 1
                    self.pay_back_time_remaining += 1
                    return False

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

    def fine_money(self, level, money=None):
        if money is None:
            if level == 0:
                m = 1000
            elif level == 1:
                m = 3000
            elif level == 2:
                m = 5000
        else:
            m = money
        if self.cash >= m:
            self.cash -= m
        else:
            self.loaned_money += m
            self.pay_back_time_remaining += 1
            self.pay_back_time_total += 1
        return m

    def bankrupt(self):
        if self.money_to_pay() > self.get_money():
            return True
        return False

