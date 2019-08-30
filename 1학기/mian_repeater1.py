#p153
#import repeater
#from repeater import repeat, once
#from repeater import * #이름 생략가능
import repeater as re #이름을 지어 넣을 수 있음
s = input("반복할 문자를 입력해주세요 : ")
n = input("반복 횟수를 입력해주세요 :")
# repeater.repeat(s, int(n))
# repeater.repeat(s)
# repeater.once(s)
re.repeat(s, int(n))
re.repeat(s)
re.once(s)