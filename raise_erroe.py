class Mobile:
    def __init__(self, name):
        self.name = name

class Mobile_Shop:
    def __init__(self):
        self.mobile_list = []

    def add_mobile(self, mobile):
        if isinstance(mobile, Mobile):
            self.mobile_list.append(mobile)
        else:
            raise TypeError

mb = Mobile("Samsung")
mb_shop = Mobile_Shop()
# mb_shop.add_mobile("OnePlues") string will raised the type error
mb_shop.add_mobile(mb)
print(mb_shop.mobile_list[0].name)