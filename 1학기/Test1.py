#학번 -> 학년 학과 반 번호
print("학번을 입력하시오 : ")
sn = input()
g = sn[0]
c = sn[1]
a = sn[2]
b = sn[3]

if g == "1" or g == "2":
    if c =="1" or c == "2":
        print("뉴미디어소프트웨어과")
    elif c == "3" or c == "4":
        print("뉴미디어웹솔루션과") 
    elif c == "5" or c == "6":
        print("뉴미디어 디자인과")
elif g == "3":
    if c == "1" or c == "2":
        print("인터랙티브미디어과")
    elif c == "3" or c == "4":
        print("뉴미디어 디자인과")
    elif c == "5" or c == "6":
        print("뉴미디어솔루션과")
print(g,"학년",c,"반",a,b,"번 입니다.")
