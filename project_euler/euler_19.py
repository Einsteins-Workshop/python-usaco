# https://projecteuler.net/problem=19

# You are given the following information, but you may prefer to do some research for yourself.
#
# 1 Jan 1900 was a Monday.
# Thirty days hath September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
day=1
date=1
month=1
year=1901
def isLeap(y):
    if y%4==0:
        if y%100!=0 or y%400==0:
            return True
        else:
            return False
    else:
        return False
def monthLength(m, y):
    if m==9 or m==4 or m==6 or m==11:
        return 30
    if m==2:
        if isLeap(y):
            return 29
        else:
            return 28
    else:
        return 31
def daysFromJanFirst1900(d, m, y):
    daysTotal=0
    for ye in range(1900,y):
        if isLeap(ye):
            daysTotal=daysTotal+366
        else:
            daysTotal=daysTotal+365
    for mo in range(1,m):
        daysTotal=daysTotal+monthLength(mo, y)
    daysTotal=daysTotal+d-1
    return daysTotal
def isSunday(d, m, y):
    return daysFromJanFirst1900(d,m,y)%7==6
def tomorrow(d,m,y):
    nd=d
    nm=m
    ny=y
    nd=d+1
    if nd>monthLength(m,y):
        nd=1
        nm=m+1
    if nm>12:
        nm=1
        ny=y+1
    return [nd,nm,ny]
sundaysOn1st=0

while day<=31 and month<=12 and year<=2000:
    if month==1 and isSunday(day,month,year):
        sundaysOn1st=sundaysOn1st+1
    tomorrowing=tomorrow(day,month,year)
    day=tomorrowing[0]
    month=tomorrowing[1]
    year=tomorrowing[2]
    print(day,month,year)
print(sundaysOn1st)
while True:
    print(isSunday(int(input("D?:")),int(input("M?:")),int(input("Y?:"))))