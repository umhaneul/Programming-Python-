from datetime import datetime

print("현재 날짜 시각 객체 얻기")
today = datetime.now()
print("today = datetime.now = ", today)
print("년 월 일 : ", today.year, today.month, today.day)
print("시 분 초 : ", today.hour, today.minute, today.second)
print("요일 : ",today.weekday())
print("특정 날짜 시각 객체 만들기")
day = datetime(2019, 1, 1, 0, 0, 0)     #2019년 1월 1일 0시 0분 0초
print("day = datetime(2019, 1, 1, 0,0, 0) : ",day)
print("2019년부터 지나온 시간 구하기")
print("today - day : ", today - day)

#태어난지 며칠?
print("테어난지 며칠?",today - datetime(2002, 7, 6, 12, 0, 0))

#올해 크리스마스 며칠 남았는지?
print("올해 크리스마스 며칠 남았는지?",today - datetime(2019, 12, 25, 0, 0, 0))

#내 생일 며칠 남았는지?
print("내 생일 며칠 남았는지?",today - datetime(2002, 7, 6, 0, 0, 0))