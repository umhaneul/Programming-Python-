# from foods.drinks import milk
# milk.drink()

# from foods.drinks.milk import drink #import에 모듈이 들어갈 수 있고 패키지가 들어갈 수 있다
# drink()

# import foods.drinks.milk
# foods.drinks.milk.drink()
# import foods
# foods.drinks.milk.drink()

# import foods.drinks.milk
# foods.drinks.milk.drink()

# from foods.drinks.milk import drink #import에 쓴것은 다 나와야됨 ex)drink()
# drink()

# import foods.drinks.milk
# foods.drinks.milk.drink()

#foods,drinks.milk.drink() #error

#from: 폴더 or 모듈
#import: 모둘 or 함수

from foods.drinks import milk as m
m.drink()