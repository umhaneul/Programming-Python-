from idlelib import history

from order import Order
from file_manager2 import fileManager

# 주문내역 불러오고, 출력하자
file_manager = FileManager("history.bin")
histroy = file_manager.load()
if len(history) == 0:
    print("주문내역이 없습니다.")
#else:
for h in history:
    print(h)
    sum += h.price
print("내가 아마스빈에 갖다 바친 돈 : "+str(sum)+"원")

# 지금 주문하자
o = Order()
o.order_drink()

# 주문내역 저장하자
file_manager.save(history + o.order_menu)