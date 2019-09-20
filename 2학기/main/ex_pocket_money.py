#국어, 영어, 수학, 자바, 파이썬, JSP
kor = input("국어 점수를 입력해 주세요 :")
eng = input("영어 점수를 입력해 주세요 : ")
mat = input("수학 점수를 입력해 주세요 : ")
java = input("자바 점수를 입력해 주세요 : ")
py = input("파이썬 점수를 입력해 주세요 : ")
jsp = input("JSP 점수를 입력해 주세요 :")

#총점 평균 구하기
sum = int(kor)+int(eng)+int(mat)+int(java)+int(py)+int(jsp)
print("총점은 :",sum,"입니다.")
avg = sum/6
print("평균은 : ",round(avg,2),"입니다.")
#용돈 구하기
# 90점이상 100000원
if(avg>=90) :
    print("용돈 100000원 입니다.")
# 80점이상 80000원
elif(avg>=80) :
    print("용돈은 80000원 입니다.")
# 70점이상  70000원
elif(avg>=70) :
    print("용돈은 70000원 입니다.")
# 60점이상 60000원
elif(avg>=60) :
    print("용돈은 60000원 입니다.")
# 그 미만 50000원
else :
    print("용돈은 50000원 입니다.")
