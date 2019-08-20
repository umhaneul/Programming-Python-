#아마스빈 주문 앱
#Drink <- Coffe
#      <- Bubbletea
#Order
# 메뉴 보여주자
# 음료 주문하자
# 주문한 음료 보여주자
# 총 금액 계산하자
from coffee import Coffee
from bubbletea import Bubbletea

class Order :
    _menus = [Coffee("아메리카노",1800), Bubbletea("딸기요거트",3500)]
    def __init__(self) :
        self.order_menu = []
        self.order = None

    def show_menu(self) :
        print("0:아메리카노 1800원, 1:딸기요거트 3500원")

    def sum_price(self) :
        sum = 0
        for drink in self.order_menu:
            sum += drink.price
        
        return sum

    def order_drink(self) :
        #반복▼
        while True :
            # 메뉴 보여주자
            self.show_menu()
            # 주문받자
            # 음료선택하자
            self.order = input("음료를 선택하세요:")
            #음료객체생성하자
            # 0 -> Coffee("아메리카노", 1800)
            # 1 -> Bubbletea("딸기요거트",3500)
            if self.order == "":
                break    #메뉴 선택 안하고 그냥 엔터치면 주문 끝
                if int(self.order) == 0:
                    drink = Coffee("아메리카노",1800)
                elif int(self.order) == 1:
                    drink = Bubbletea("딸기요커트", 3500)
            drink = Order._menus[int(self.order)]
            # 음료옵션정하자
            drink.order()
            # 주문한 음료 리스트에 추가하자
            self.order_menu.append(drink)
        #반복▲
        #주문한 음료 출력하자
        for drink in self.order_menu:
            print(drink)
        #금액 합계구하자
        print("총 금액 : " + str(self.sum_price()) + "원")


# 아메리카노 = Coffee("아메리카노", 1800)
# 아메리카노.order()
# print(아메리카노) #이름 : 아메리카노\t가격: 1800원
# 타로밀크티 = Bubbletea("타로밀크티",3500)
# 타로밀크티.order()
# print(타로밀크티)