#p217
l = [1,2,3]
try :
    print(l[1])
    print(l[2])
   # print(l[4]) #IndexError: list index out of range
except IndexError as e: #에러를 자세히 보고 싶으면 지칭하는 변수를 지정해서 불러옴
    print("인덱스에러")
    print(e)
else :
    print("성공적으로 모든 코드를 실행")
