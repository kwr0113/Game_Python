import datetime

print(datetime.date.today())

d = datetime.datetime.now()
print(d.hour)
print(d.minute)
print(d.second)

print(d.year)
print(d.month)
print(d.day)

today = datetime.date.today()
birth = datetime.date(1998, 1, 13)
print(today - birth)