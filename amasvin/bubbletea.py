#아마스빈 주문 앱
#Drink <- Coffe
#      <- Bubbletea
#Order
# 메뉴 보여주자
# 음료 주문하자
# 주문한 음료 보여주자
# 총 금액 계산하자
from drink import Drink

class Bubbletea(Drink) :
    _pearls = ["타피오카", "코코", "젤리", "알로에"]
    def __init__(self,name,price):
        super().__init__(name,price)
        self.pearl = 0

    def set_pearl(self) :
        self.pearl = input("펄을 선택하세요(0:타피오카, 1:코코, 2:젤리, 3:알로에)")
        if self.pearl == "":
            self.pearl = 0
        else :
            self.pearl = int(self.pearl)

    def __str__(self):
        return super().__str__() + "\t펄:" + Bubbletea._pearls[self.pearl]   

    def order(self) :
        super().order()
        self.set_pearl

# 아메리카노 = Coffee("아메리카노", 1800)
# 아메리카노.order()
# print(아메리카노) #이름 : 아메리카노\t가격: 1800원
# 타로밀크티 = Bubbletea("타로밀크티",3500)
# 타로밀크티.order()
# print(타로밀크티)