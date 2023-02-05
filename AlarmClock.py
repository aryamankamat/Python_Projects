from os import *
from datetime import *
from time import *

print("\nEnter the Date and Time in standered format.\n")
a, b, c = input("Enter the date : ").split('/')
y = int(c)
m = int(b)
d = int(a)
# print(d)
# print(m)
# print(y)
hr, mn, sec = input("Enter the time : ").split(':')
# print(hr)
# print(mn)
# print(sec)
schedule = date(y, m, d)
# n = 1
while True:
    if localtime().tm_hour == int(hr) and localtime().tm_min == int(mn) and localtime().tm_sec == int(sec) and date.today() == schedule:
        print("Alarm is ringing...")
        startfile(r"C:\Users\Hp\Downloads\Dhokha.mp3")
        break
    else:
        # n = n + 1
        pass
