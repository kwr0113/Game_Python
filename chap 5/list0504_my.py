# 시간 경쟁 게임 Time Attack
# 알파벳 찾기
import random
import datetime

ALP = [
    'A', 'B', 'C', 'D', 'E',
    'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z']
r = random.choice(ALP)
alp = ''

for i in ALP:
    if i != r:
        alp = alp + i

print(alp)
st = datetime.datetime.now()
ans = input("빠진 알파벳은? ")

while True:
    if ans == r.lower():
        print("정답입니다!")
        et = datetime.datetime.now()
        print((et-st).seconds, '초 걸렸습니다')
        break
    else:
        ans = input('틀렸습니다ㅜ   ')
