#input("현재의 input() 함수는 사용자 정의 함수입니다.")

def input(s):
    print(s)

input("현재의 input() 함수는 사용자 정의 함수입니다.")

import random

#n = random.randrange(1 ,6+1) #1<= x <=6+1 랜덤수 x 리턴
def rolling_dice():
    n = random.randint(1 ,6) #1<= x <=6 랜덤수 x 리턴
    print("6면 주사위 굴린 결과 : ",n)
rolling_dice()
rolling_dice()


#star함수 정의

def star():
    print("*****")
star() #*****
star() #*****
star() #*****

def rolling_dice(pip):
    n = random.randint(1, pip)
    print(pip, "면 주사위 굴린 결과 : ",n)

#rolling_dice()
rolling_dice(4)
rolling_dice(6)
rolling_dice(6)
rolling_dice(8)
rolling_dice(10)
rolling_dice(12)
rolling_dice(20)

def rolling_dice(pip, repeat) :
    for r in range(1, repeat+1) :
        n = random.randint(1, pip)
        print(pip,"면 주사위 굴린 결과 : ",r," :",n)
    
#rolling_deice()
rolling_dice(6,1)
rolling_dice(6,2)
rolling_dice(12,0)
rolling_dice(20,-3)

#가변인수
print("가변인수--------------------")
print("♡")
print("♡","♪")
print("♡","♪","♣")
print("♡","♪","♣","♠")
print("♡","♪","♣","♠","★")

#def p(*args):
    #string = " "
    #for a in args:
       # string += a
    #print(string)
#p("♡")
#p("♡","♪","♣","♥")

#안녕()함수를 만들고,

def 안녕(*args) :
    for a in args :
       print("안녕,",a)
       

안녕("가연아","수빈아","정윤아")
#안녕, 가연아
#안녕, 수빈아
#안녕, 정윤아

#def p(space, space_num, *args) : *args는 앞에 있을 수 없음
def P(*args,space, sapce_num):
        string = args[0]
        for i in range(1 ,len(args)):
                string += (space * space_num) + args[i]
        print(string)

#p(" ",3,"♡","♪")
#p("☆",2,"♡","♣")
#p("_",3,"♡","♣","♠")

#p115 혼자해보기
def star(word, *args):
        for i in args:
                 print(word*i)

star("♬",3)
star("♡",1,2,3)

#p116 키워드 인자를 사용한 함수
def fn(a,b,c,d,e):
        print(a,b,c,d,e)
fn(1,2,3,4,5)
fn(10,20,30,40,50)
fn(5,6,7,8,9)
fn(a=1,b=2,c=3,d=4,e=5)
fn(1,2,c=3,e=3,d=5)
#fn(d=4,e=5,1,2,3)

def fn(a, b, c, *d):
        print(a,b,c,d)

#fn(c=3,b=2,a=1;,4,5)
#fn(c=3, b=2, a=1,4,5)
#fn(s,5,a=1,b=2,c=3)    

#p118 혼자해보기
def star(mark, repeat,soace,sapace_num,line):
        for i in range(1, line):
         str = (mark * repeat)
        for j in range(2, repeat):
         string += (space * space_repeat) + (mark * repeat)
        print(string)

star("*",2,"+",3,5)
print("--------------")
star(mark="*",repeat=2,space="+",space_repeat=3,line=5)

def star2(mark, repeat, space, space_repeat, line):
        string = (mark*repeat)+(space*space_repeat)+(mark*repeat)
        for n in range(line):
                print(string)

star2("X",3, "_", 2, 3)
print("----------------------")
star2(mark="X",repeat=3, space="_", space_repeat=2, line=3)