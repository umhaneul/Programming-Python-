#버스 여유, 보통, 혼잡
#탑승객, 하차객 입력받자
#0 이상 10 미만 : 여유
#10 이상 20미만 : 보통
#20 이상 : 혼잡
#1
#------
sum = 0
while True :
    in0 = input("탑승객 수는? (-1: 끝)")
    if in0 == "-1" :
        break
    in0 = int(in0)
    out = input("하차객 수는? : ")
    out = int(out)
    sum += in0 - out
#------
print("버스에 있는 사람 수는 : " ,sum)
if 0<= sum < 10 :
    print("여유")
elif 10 <= sum <20 :
    print("보통")
else :
    print("혼잡")